DBENDPOINT=`cat databaseparams.json | jq -r '.["dbendpoint"]'`
PGUSER=`cat databaseparams.json | jq -r '.["dbuser"]'`
PGPASSWORD=`cat databaseparams.json | jq -r '.["dbpassword"]'`
DBNAME=`cat databaseparams.json | jq -r '.["dbname"]'`

PGPASSWORD=$PGPASSWORD psql -h $DBENDPOINT -U $PGUSER -p 5432 lidarbuilding -f ../../data/dc_building_sql_statements_test.sql
PGPASSWORD=$PGPASSWORD psql -h $DBENDPOINT -U $PGUSER -p 5432 lidarbuilding -f ../../data/dc_building_sql_statements_training.sql