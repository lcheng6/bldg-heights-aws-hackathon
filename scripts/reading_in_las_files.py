import numpy as np
from laspy.file import File
from pandas import DataFrame
from geopandas import GeoDataFrame
from shapely.geometry import Point
import requests

# # Download LAS file, all of which are downloadable through https
# url = "https://dc-lidar-2018.s3.amazonaws.com/Classified_LAS/1120.las"
# r = requests.get(url)
#
# with open("data/python-1120.las", 'wb') as f:
#     f.write(r.content)

#Read in LAS file
inFile = File("../data/1120.las", mode = "r")

#Import LAS into numpy array (X=raw integer value x=scaled float value)
#Note that the columns specifications are slightly different
lidar_points = np.array((inFile.X,inFile.Y,inFile.Z,inFile.intensity,
                          inFile.classification, inFile.gps_time, 
                          inFile.overlap, inFile.scan_angle )).transpose()

#Transform to pandas DataFrame
lidar_df=DataFrame(lidar_points, columns = ["X","Y","Z","intensity",
                "classification","gps_time","overlap","scan_angle"])

#Transform to geopandas GeoDataFrame
crs = None
geometry = [Point(xyz) for xyz in zip(inFile.X,inFile.Y,inFile.Z)]
lidar_geodf = GeoDataFrame(lidar_df, crs=crs, geometry=geometry)

# set correct coordinate reference system
# the LIDAR data's EPSG must be 6487
lidar_geodf.crs = {'init': 'epsg:6487'}

# reproject to CRS 4326 (Same as building footrpint data) 
lidar_geodf['geometry'] = lidar_geodf['geometry'].to_crs(epsg=4326)