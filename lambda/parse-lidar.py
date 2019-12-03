import sys
import numpy as np
from laspy.file import File
from pandas import DataFrame
from geopandas import GeoDataFrame
from shapely.geometry import Point
import requests


# Read in LAS file
inFile = File(sys.argv[1], mode = "r")

# Import LAS into numpy array (X=raw integer value x=scaled float value)
# Note that the columns specifications are slightly different
lidar_points = np.array((inFile.X, inFile.Y, inFile.Z, inFile.intensity,
                          inFile.classification, inFile.gps_time,
                          inFile.overlap, inFile.scan_angle )).transpose()


columns = ["X", "Y", "Z", "intensity", "classification","gps_time","overlap","scan_angle"]

# Transform to pandas DataFrame
lidar_df=DataFrame(lidar_points, columns = columns)
crs = None
geometry = [Point(xyz) for xyz in zip(inFile.X/1000,inFile.Y/1000,inFile.Z)]
lidar_geodf = GeoDataFrame(lidar_df, crs=crs, geometry=geometry)

# set correct coordinate reference system
lidar_geodf.crs = {'init': 'epsg:6487'}

# reproject to CRS 4326 (Same as building footrpint data)
lidar_geodf['geometry'] = lidar_geodf['geometry'].to_crs(epsg=4326)

columns_str = ", ".join(columns)

# Create output SQL.
sql = f"insert into lidar_values (ground_coord, z, intensity, classification, gps_time, overlap, scan_angle) VALUES "

# Depending on the DF size you could potentially chunk here to reduce the file sizes.
row = 0
for idx, frame in lidar_geodf.iterrows():
    row += 1
    x, y, z, intensity, classification, gps_time, overlap, scan_angle, geom = frame.to_list()
    x, y, z = geom.x, geom.y, geom.z #  Replace the old CRS values and move this over.
    items = [f"'POINT({x} {y} {z})'::geometry", z, intensity, classification, gps_time, overlap, scan_angle]
    items_str = map(str, items)
    values = ', '.join(items_str)
    sql += f"({values}),"

sql = f"{sql[:-1]};"

# Output the file, which we map to a file
print(sql)