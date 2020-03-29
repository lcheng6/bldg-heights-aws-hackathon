import json

def process_single_feature(feature):
    processed_feature = {}
    processed_feature["EGID"] = feature["properties"]["EGID"]
    processed_feature["ROOF_TYPE"] = feature["properties"]["ROOF_TYPE"]
    processed_feature["Shape_Length"] = feature["properties"]["Shape_Length"]
    processed_feature["Shape_Area"] = feature["properties"]["Shape_Area"]
    if ("ALTITUDE_M" in feature["properties"]):
        processed_feature["ALTITUDE_M"] = feature["properties"]["ALTITUDE_M"]
    processed_feature["geometry"] = feature["geometry"]
    processed_feature["geometry"]["coordinates"] = processed_feature["geometry"]["coordinates"]
    return processed_feature

def form_training_insert_statement(processed_feature, dbname):
    EGID = processed_feature["EGID"]

    Shape_Area = processed_feature["Shape_Area"]
    RoofType = processed_feature["ROOF_TYPE"]
    Shape_Length = processed_feature["Shape_Length"]
    sql_statement = f"""
insert into {dbname} (EGID, Shape_Area, RoofType, Shape_Length, Border)
VALUES (
    '{EGID}',
    '{Shape_Area}',
    '{RoofType}',
    '{Shape_Length}',
    ST_GeomFromGeoJSON(
        '{{
            "type": "{processed_feature["geometry"]["type"]}",
            "coordinates": {processed_feature["geometry"]["coordinates"]}
        }}'
    )
);
    """
    return sql_statement

def form_test_insert_statement(processed_feature, dbname):
    EGID = processed_feature["EGID"]

    Shape_Area = processed_feature["Shape_Area"]
    Altitude_M = processed_feature["ALTITUDE_M"]
    RoofType = processed_feature["ROOF_TYPE"]
    Shape_Length = processed_feature["Shape_Length"]
    sql_statement = f"""
insert into {dbname} (EGID, Shape_Area, Altitude_M, RoofType, Shape_Length, Border)
VALUES (
    '{EGID}',
    '{Shape_Area}',
    '{Altitude_M}',
    '{RoofType}',
    '{Shape_Length}',
    ST_GeomFromGeoJSON(
        '{{
            "type": "{processed_feature["geometry"]["type"]}",
            "coordinates": {processed_feature["geometry"]["coordinates"]}
        }}'
    )
);
    """
    return sql_statement

traing_sql_output = open("../data/dc_building_sql_statements_training.sql", "w")

with open('../data/DC_buildings_Footprint_4326_training.geojson') as json_file:
    data = json.load(json_file)
    features = data["features"]
    # print ("count of features: ", len(features))


    for feature in features:
        processed_feature_example = process_single_feature(feature)
        # print (processed_feature_example)

        sql_example = form_training_insert_statement(processed_feature_example, "buildinginfotraining")
        traing_sql_output.write(sql_example)


test_sql_output = open("../data/dc_building_sql_statements_test.sql", "w")

with open('../data/DC_buildings_Footprint_4326_test.geojson') as json_file:
    data = json.load(json_file)
    features = data["features"]
    # print ("count of features: ", len(features))


    for feature in features:
        processed_feature_example = process_single_feature(feature)
        # print (processed_feature_example)

        sql_example = form_test_insert_statement(processed_feature_example, "buildinginfotest")
        test_sql_output.write(sql_example)