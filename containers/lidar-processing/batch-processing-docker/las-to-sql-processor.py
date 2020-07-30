import numpy as np
from laspy.file import File
from pandas import DataFrame
from geopandas import GeoDataFrame
from shapely.geometry import Point
import requests
import os
import lasutility
import argparse

import boto3 # like, are we not going to use boto3 in python on AWS?
from botocore.exceptions import ClientError

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--laskey", help="LAS file key name")
args = parser.parse_args()

def download_las_data(keyname):
    url = lasutility.https_path_from_keyname(keyname)
    lidar_data = requests.get(url)
    lasdatafile = f"/tmp/{keyname}"
    with open(lasdatafile, "wb+") as f:
        f.write(lidar_data.content)

def cleanup_las_data(keyname):
    lasdatafile = f"/tmp/{keyname}"
    os.remove(lasdatafile)

def convert_las_data_to_sql_statement(keyname, max_rows_per_iteration = 50000):
    #we need to partition the GeoDataFrame.to_crs function to 10,000 blocks, otherwise jupyter seem to have memory errors
    #might need to come back to this and recheck
    lasdatafile = f"/tmp/{keyname}"
    keysequencenum = keyname.split('.')[0] #get the #### of the file "####.las"
    lassqlfile = f"/tmp/{keysequencenum}.sql"
    lascsvfile = f"/tmp/{keysequencenum}.csv"
    inFile = File(lasdatafile)
    row_count = 0

    lidar_points = np.array((inFile.X,inFile.Y,inFile.Z,inFile.intensity,
                             inFile.classification, inFile.gps_time,
                             inFile.overlap, inFile.scan_angle,
                             inFile.x, inFile.y, inFile.z,
                             inFile.Synthetic, inFile.Withheld)).transpose()
    lidar_df=DataFrame(lidar_points, columns = ["X","Y","Z","intensity",
                                                "classification","gps_time",
                                                "overlap","scan_angle",
                                                "x", "y", "z",
                                                "synthentic", "withheld"])

    lidar_df_total_length = lidar_df.shape[0]
    sql_lines_array = []
    csv_lines_array = []
    sql_preamble = f"insert into lidar_values (ground_coord, z, intensity, classification, gps_time, overlap, scan_angle, synthetic, withheld, dcoctocode) VALUES"

    sql_file = open(lassqlfile, "w")
    csv_file = open(lascsvfile, "w")

    for lidar_idx_start in range(0, lidar_df_total_length, max_rows_per_iteration):
        lidar_idx_end = lidar_idx_start + max_rows_per_iteration
        lidar_idx_end = min(lidar_idx_end, lidar_df_total_length)
        lidar_indices_curr_iter = np.arange(lidar_idx_start, lidar_idx_end)
        lidar_df_sampled = lidar_df.iloc[lidar_indices_curr_iter]

        geometry_sampled = [Point(xyz) for xyz in zip(lidar_df_sampled.x,lidar_df_sampled.y,lidar_df_sampled.z)]

        crs = None
        lidar_geodf_sampled = GeoDataFrame(lidar_df_sampled, crs=crs, geometry=geometry_sampled)
        lidar_geodf_sampled.crs = {'init': 'epsg:26985'}
        lidar_geodf_sampled['geometry'] = lidar_geodf_sampled['geometry'].to_crs(epsg=4326)

        for idx, frame in lidar_geodf_sampled.iterrows():
            row_count+=1
            X, Y, Z, intensity, classification, gps_time, overlap, scan_angle, x, y, z, synthetic, withheld, geom = frame.to_list()
            lat, long, z = geom.x, geom.y, geom.z #  Replace the old CRS values and move this over.
            items = [f"'POINT({lat} {long} {z})'::geometry", z, intensity, int(classification), gps_time, overlap, scan_angle, int(synthetic), int(withheld), int(keysequencenum)]
            items_str = map(str, items)
            sql_line = '(' + ', '.join(items_str) + ')'
            sql_lines_array.append(sql_line)

            items_str = map(str, items)
            csv_line = ', '.join(items_str)
            csv_lines_array.append(csv_line)

        sql_complete_statement = sql_preamble + "\n" + (",\n".join(sql_lines_array)) + ';' + "\n"
        sql_file.write(sql_complete_statement)

        csv_complete_statement = "\n".join(csv_lines_array) + "\n"
        csv_file.write(csv_complete_statement)
        #reset the sql_lines_array
        sql_lines_array = []
        csv_lines_array = []

    sql_file.close()

    return row_count # return the number of entries created

def upload_las_data_to_s3_bucket(keyname, s3bucket, s3prefix):
    s3_client = boto3.client('s3')
    local_path = f"/tmp/{keyname}"
    object_name = f"{s3prefix}/{keyname}"
    try:
        response = s3_client.upload_file(local_path, s3bucket, object_name)
    except ClientError as e:
        return False
    return True

def las_to_sql(laskeyname):
    download_las_data(laskeyname)
    row_count = convert_las_data_to_sql_statement(laskeyname)
    print(row_count)
    cleanup_las_data(laskeyname)

    keysequencenum = laskeyname.split('.')[0] #get the #### of the file "####.las"
    sqlfilename = f"{keysequencenum}.sql"
    csvfilename = f"{keysequencenum}.csv"
    upload_las_data_to_s3_bucket(sqlfilename, "urban-institute-datasets", "bldg-height/las-sql-statements-v2-1")
    upload_las_data_to_s3_bucket(csvfilename, "urban-institute-datasets", "bldg-height/las-csv-statements-v2-1")

if __name__ == "__main__":
    las_to_sql(args.laskey)