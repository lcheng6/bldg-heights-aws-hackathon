import json
import os

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
  os.system(f"python3 ./convert_ms_us_bldg_geojson_file_into_postgres_statements.py --state {state}")
  pass

def insert_geojson_into_db():
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

    if (state == "Alaska"):
      break
