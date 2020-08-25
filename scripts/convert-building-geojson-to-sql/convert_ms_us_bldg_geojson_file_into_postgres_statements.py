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

def form_insert_into_statement(dbname):
    sql_statement = f"""
insert into {dbname} (State, Border)
VALUES """
    return sql_statement

def form_single_value_sql_statement(processed_feature):
    statename = processed_feature["statename"]
    sql_statement = f"""
    ( '{statename}',
    ST_GeomFromGeoJSON(
        '{{
            "type": "{processed_feature["geometry"]["type"]}",
            "coordinates": {processed_feature["geometry"]["coordinates"]}
        }}')
    )"""
    return sql_statement


# building_list_file = json.load("../../data/microsoft-building-footprint/ms-us-building-listing.json")

def convert_single_state_file_from_json_to_sql(state="Virginia", max_rows_per_iteration=5000):

    traing_sql_output = open("../../data/microsoft-building-footprint/Virginia.sql", "w")

    with open('../../data/microsoft-building-footprint/Virginia.geojson') as json_file:
        data = json.load(json_file)
        features = data["features"]
        # print ("count of features: ", len(features))

        feature_total_length = len(features)
        sql_preamble = form_insert_into_statement("ms_building_borders")
        for feature_idx_start in range (0, feature_total_length, max_rows_per_iteration):
            feature_idx_end = min(feature_idx_start + max_rows_per_iteration, feature_total_length)
            features_subarray = features[feature_idx_start: feature_idx_end]
            sql_statement_arrays = []
            for single_feature in features_subarray:
                single_processed_feature = process_single_feature(single_feature, state)
                single_feature_sql_statement = form_single_value_sql_statement(single_processed_feature)
                sql_statement_arrays.append(single_feature_sql_statement)


            sql_complete_statement = sql_preamble + "\n" + (",".join(sql_statement_arrays)) + ';' + "\n"
            traing_sql_output.write(sql_complete_statement)

        # for feature in features:
        #     processed_feature_example = process_single_feature(feature, "Virginia")
        #     # print (processed_feature_example)
        #
        #     sql_example = form_us_building_insert_statement(processed_feature_example, "usbuilding")
        #     traing_sql_output.write(sql_example)


convert_single_state_file_from_json_to_sql()