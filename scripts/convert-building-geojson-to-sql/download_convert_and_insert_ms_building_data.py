import json
import os
import boto3

def download_building_zip_file(state, zip_path):

  statename_without_spaces = "".join(state.split())
  os.system(f"wget -O ../../data/microsoft-building-footprint/{statename_without_spaces}.zip {zip_path}")
  stored_zip_file = f"../../data/microsoft-building-footprint/{statename_without_spaces}"
  return stored_zip_file

def unzip_building_zip_file(state):
  statename_without_spaces = "".join(state.split())
  os.system(f"unzip -o ../../data/microsoft-building-footprint/{statename_without_spaces}.zip -d ../../data/microsoft-building-footprint/")
  pass

def convert_geojson_to_sql_file(state):
  os.system(f"python3 ./convert_ms_us_bldg_geojson_file_into_postgres_statements.py --state '{state}'")
  pass

def insert_geojson_into_db(state):
  statename_without_spaces = "".join(state.split())

  secretsmanager_client = boto3.client('secretsmanager')
  dbSecretValues = secretsmanager_client.get_secret_value(SecretId='UrbanInstituteDevRDSParameter')
  dbSecretValuesJson = json.loads(dbSecretValues['SecretString'])
  POSTGRES_ADDRESS = dbSecretValuesJson['POSTGRES_ADDRESS'] ## INSERT YOUR DB ADDRESS IF IT'S NOT ON PANOPLY
  POSTGRES_PORT = int(dbSecretValuesJson['POSTGRES_PORT'])
  POSTGRES_USERNAME = dbSecretValuesJson['POSTGRES_USERNAME'] ## CHANGE THIS TO YOUR PANOPLY/POSTGRES USERNAME
  POSTGRES_PASSWORD = dbSecretValuesJson['POSTGRES_PASSWORD'] ## CHANGE THIS TO YOUR PANOPLY/POSTGRES PASSWORD POSTGRES_DBNAME = 'database' ## CHANGE THIS TO YOUR DATABASE NAME
  POSTGRES_DBNAME = dbSecretValuesJson['POSTGRES_DBNAME']

  os.system(f"PGPASSWORD={POSTGRES_PASSWORD} psql -h {POSTGRES_ADDRESS} -U {POSTGRES_USERNAME} -p {POSTGRES_PORT} {POSTGRES_DBNAME} -f ../../data/microsoft-building-footprint/{statename_without_spaces}.sql")
  pass

def delete_zip_geojson_and_sql_files(state):
  statename_without_spaces = "".join(state.split())
  os.system(f"rm -f ../../data/microsoft-building-footprint/{statename_without_spaces}.zip")
  os.system(f"rm -f ../../data/microsoft-building-footprint/{statename_without_spaces}.geojson")
  os.system(f"rm -f ../../data/microsoft-building-footprint/{statename_without_spaces}.sql")
  pass

with open("../../data/microsoft-building-footprint/ms-us-building-listing.json") as json_file:
  ms_building_list = json.load(json_file)

  for state, zip_path in ms_building_list.items():
    print (state + "," + zip_path)
    download_building_zip_file(state=state, zip_path=zip_path)
    unzip_building_zip_file(state=state)
    convert_geojson_to_sql_file(state=state)
    insert_geojson_into_db(state=state)
    delete_zip_geojson_and_sql_files(state=state)

    # if (state == "Alaska"):
    #   break
