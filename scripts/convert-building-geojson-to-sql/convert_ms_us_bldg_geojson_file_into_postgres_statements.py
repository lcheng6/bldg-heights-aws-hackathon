#this particular python is only useful for the DC building data which was used during
#the original AWS hackathon.  As this file make use of EGID, ROOF_TYPE etc, it's not useful for the
#Microsoft US Building dataset. 
import json
import argparse

def process_single_feature(feature, statename):
    processed_feature = {}
    processed_feature["statename"] = statename
    processed_feature["geometry"] = feature["geometry"]
    processed_feature["geometry"]["coordinates"] = processed_feature["geometry"]["coordinates"]
    return processed_feature

def form_us_building_insert_statement(processed_feature, dbname):
    statename = processed_feature["statename"]
    sql_statement = f"""
insert into {dbname} (State, Border)
VALUES (
    '{statename}',
    ST_GeomFromGeoJSON(
        '{{
            "type": "{processed_feature["geometry"]["type"]}",
            "coordinates": {processed_feature["geometry"]["coordinates"]}
        }}'
    )
);
    """
    return sql_statement


# building_list_file = json.load("../../data/microsoft-building-footprint/ms-us-building-listing.json")

traing_sql_output = open("../../data/microsoft-building-footprint/Virginia.sql", "w")

with open('../../data/microsoft-building-footprint/Virginia.geojson') as json_file:
    data = json.load(json_file)
    features = data["features"]
    # print ("count of features: ", len(features))


    for feature in features:
        processed_feature_example = process_single_feature(feature, "Virginia")
        # print (processed_feature_example)

        sql_example = form_us_building_insert_statement(processed_feature_example, "usbuilding")
        traing_sql_output.write(sql_example)


