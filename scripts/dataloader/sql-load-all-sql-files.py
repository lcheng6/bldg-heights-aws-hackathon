import lasutility
# import boto3

def download_sql_file_from_s3(sqlfilekeyname):
    print (sqlfilekeyname)
    pass
    # s3_client = boto3.s3

def download_las_data_to_s3_bucket(keyname, s3bucket, s3prefix):
    s3_client = boto3.client('s3')
    local_path = f"./lasdata/{keyname}"
    object_name = f"{s3prefix}/{keyname}"
    try:
        response = s3_client.upload_file(local_path, s3bucket, object_name)
    except ClientError as e:
        return False
    return True

def mainfunction():
    laskeynames = lasutility.get_las_file_names()
    laskeynames = laskeynames[0, 1, 2]
    for laskeyname in laskeynames:
        keysequencenum = laskeyname.split('.')[0] #get the #### of the file "####.las"
        sqlfilename = f"{keysequencenum}.sql"
        download_sql_file_from_s3(sqlfilename, "additional-test-datasets", "bldg-height/las-sql-statements")

mainfunction()
