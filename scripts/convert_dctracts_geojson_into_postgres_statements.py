import json

def process_single_feature(feature):
  processed_feature = {}
  processed_feature["STATEFP"] = feature["properties"]["STATEFP"]
  processed_feature["COUNTYFP"] = feature["properties"]["COUNTYFP"]
  processed_feature["TRACTCE"] = feature["properties"]["TRACTCE"]
  processed_feature["GEOID"] = feature["properties"]["GEOID"]
  processed_feature["NAME"] = feature["properties"]["NAME"]
  processed_feature["NAMELSAD"] = feature["properties"]["NAMELSAD"]
  processed_feature["MTFCC"] = feature["properties"]["MTFCC"]
  processed_feature["FUNCSTAT"] = feature["properties"]["FUNCSTAT"]
  processed_feature["ALAND"] = feature["properties"]["ALAND"]
  processed_feature["AWATER"] = feature["properties"]["AWATER"]
  processed_feature["INTPTLAT"] = feature["properties"]["INTPTLAT"]
  processed_feature["INTPTLON"] = feature["properties"]["INTPTLON"]

  processed_feature["geometry"] = feature["geometry"]
  processed_feature["geometry"]["coordinates"] = processed_feature["geometry"]["coordinates"]
  return processed_feature

def form_insert_statement(processed_feature, tablename):
  STATEFP = processed_feature["STATEFP"]
  COUNTYFP = processed_feature["COUNTYFP"]
  TRACTCE = processed_feature["TRACTCE"]
  GEOID = processed_feature["GEOID"]
  NAME = feature["properties"]["NAME"]
  NAMELSAD = feature["properties"]["NAMELSAD"]
  MTFCC = feature["properties"]["MTFCC"]
  FUNCSTAT = feature["properties"]["FUNCSTAT"]
  ALAND = feature["properties"]["ALAND"]
  AWATER = feature["properties"]["AWATER"]
  INTPTLAT = feature["properties"]["INTPTLAT"]
  INTPTLON = feature["properties"]["INTPTLON"]

  sql_statement = f"""
insert into {tablename} (STATEFP, COUNTYFP, TRACTCE, GEOID, NAME, NAMELSAD, MTFCC, FUNCSTAT, ALAND, AWATER, INTPTLAT, INTPTLON, Border)
VALUES (
    '{STATEFP}',
    '{COUNTYFP}',
    '{TRACTCE}',
    '{GEOID}',
    '{NAME}',
    '{NAMELSAD}',
    '{MTFCC}',
    '{FUNCSTAT}',
    {ALAND},
    {AWATER},
    '{INTPTLAT}',
    '{INTPTLON}',
    ST_GeomFromGeoJSON(
        '{{
            "type": "{processed_feature["geometry"]["type"]}",
            "coordinates": {processed_feature["geometry"]["coordinates"]}
        }}'
    )
);
    """
  return sql_statement


traing_sql_output = open("../data/dc_tracts.sql", "w")

with open('../data/dc_tracts.geojson') as json_file:
  data = json.load(json_file)
  features = data["features"]
  # print ("count of features: ", len(features))


  for feature in features:
    processed_feature_example = process_single_feature(feature)
    # print (processed_feature_example)

    sql_example = form_insert_statement(processed_feature_example, "dctracts")
    traing_sql_output.write(sql_example)

