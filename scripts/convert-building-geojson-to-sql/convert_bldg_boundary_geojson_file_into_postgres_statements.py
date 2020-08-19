#this particular python is only useful for the DC building data which was used during
#the original AWS hackathon.  As this file make use of EGID, ROOF_TYPE etc, it's not useful for the
#Microsoft US Building dataset.
import json

def process_single_feature(feature):
    processed_feature = {}
    processed_feature["geometry"] = feature["geometry"]
    processed_feature["geometry"]["coordinates"] = processed_feature["geometry"]["coordinates"]
    return processed_feature

def form_building_insert_statement(processed_feature, dbname):
    sql_statement = f"""
insert into {dbname} (Border)
VALUES (
    ST_GeomFromGeoJSON(
        '{{
            "type": "{processed_feature["geometry"]["type"]}",
            "coordinates": {processed_feature["geometry"]["coordinates"]}
        }}'
    )
);
    """
    return sql_statement


building_boundary_sql_output = open("../../data/dc_building_sql_statements_training.sql", "w")

with open('../data/DC_buildings_Footprint_4326_training.geojson') as json_file:
    data = json.load(json_file)
    features = data["features"]
    # print ("count of features: ", len(features))


    for feature in features:
        processed_feature_example = process_single_feature(feature)
        # print (processed_feature_example)

        sql_example = form_building_insert_statement(processed_feature_example, "buildinginfotraining")
        building_boundary_sql_output.write(sql_example)


test_sql_output = open("../../data/dc_building_sql_statements_test.sql", "w")

with open('../data/DC_buildings_Footprint_4326_test.geojson') as json_file:
    data = json.load(json_file)
    features = data["features"]
    # print ("count of features: ", len(features))


    for feature in features:
        processed_feature_example = process_single_feature(feature)
        # print (processed_feature_example)

        sql_example = form_test_insert_statement(processed_feature_example, "buildinginfotest")
        test_sql_output.write(sql_example)