import numpy as np
from laspy.file import File
from pandas import DataFrame
from geopandas import GeoDataFrame
from shapely.geometry import Point
import requests
import os
import lasutility

import boto3 # like, are we not going to use boto3 in python on AWS?
from botocore.exceptions import ClientError

def las_to_sql(laskeyname):
    lasutility.download_las_data(laskeyname)
    row_count = lasutility.convert_las_data_to_sql_statement(laskeyname)
    print(row_count)
    lasutility.cleanup_las_data(laskeyname)

    keysequencenum = laskeyname.split('.')[0] #get the #### of the file "####.las"
    sqlfilename = f"{keysequencenum}.sql"
    lasutility.upload_las_data_to_s3_bucket(sqlfilename, "additional-test-datasets", "bldg-height/las-sql-statements")

