import numpy as np
from laspy.file import File
from pandas import DataFrame
from geopandas import GeoDataFrame
from shapely.geometry import Point
import requests


# Read in LAS file
inFile = File("data/python-1120.las", mode = "r")

# Import LAS into numpy array (X=raw integer value x=scaled float value)
# Note that the columns specifications are slightly different
lidar_points = np.array((inFile.X, inFile.Y, inFile.Z, inFile.intensity,
                          inFile.classification, inFile.gps_time,
                          inFile.overlap, inFile.scan_angle )).transpose()


columns = ["X","Y","Z","intensity",
                "classification","gps_time","overlap","scan_angle"]

#Transform to pandas DataFrame
lidar_df=DataFrame(lidar_points, columns = columns)

columns_str = ", ".join(columns)

sql = f"INSERT INTO lidar_values ({columns_str}) VALUES "

row = 0
for idx, frame in lidar_df.iterrows():
    row += 1
    items = map(str, frame.to_list())
    values = ', '.join(items)
    sql += f"({values}),"

    if row > 100:
        break

sql = f"{sql[:-1]};"

print(sql)