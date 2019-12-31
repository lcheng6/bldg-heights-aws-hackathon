import lasutility
import boto3
import os
import json


def download_sql_file_from_s3(sqlfilekeyname):
    return download_file_from_s3_bucket(sqlfilekeyname, "additional-test-datasets", "bldg-height/las-sql-statements")

def download_file_from_s3_bucket(keyname, s3bucket, s3prefix):
    s3 = boto3.resource('s3')
    local_path = f"/tmp/{keyname}"
    object_name = f"{s3prefix}/{keyname}"
    try:
        response = s3.meta.client.download_file(s3bucket, object_name, local_path)
    except ClientError as e:
        return False
    return True

def load_file_into_sql_server(sqlfilename):
    local_path = f"/tmp/{sqlfilename}"
def mainfunction():
    laskeynames = lasutility.get_las_file_names()
    laskeynames = laskeynames[0:2]
    for laskeyname in laskeynames:
        keysequencenum = laskeyname.split('.')[0] #get the #### of the file "####.las"
        sqlfilename = f"{keysequencenum}.sql"
        print("downloading %s", sqlfilename)
        download_sql_file_from_s3(sqlfilename)

mainfunction()
