import numpy as np
from laspy.file import File
from pandas import DataFrame
from geopandas import GeoDataFrame
from shapely.geometry import Point
import requests
import os

import boto3 # like, are we not going to use boto3 in python on AWS?
from botocore.exceptions import ClientError

for laskeyname in lasKeynames:
    download_las_data(laskeyname)
    row_count = convert_las_data_to_sql_statement(laskeyname)
    print(row_count)
    cleanup_las_data(laskeyname)

    keysequencenum = laskeyname.split('.')[0] #get the #### of the file "####.las"
    sqlfilename = f"{keysequencenum}.sql"
    upload_las_data_to_s3_bucket(sqlfilename, "additional-test-datasets", "bldg-height/las-sql-statements")

