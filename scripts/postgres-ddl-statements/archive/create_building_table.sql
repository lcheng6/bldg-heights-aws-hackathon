drop table if exists "liang-gis-test".public.buildinginfotraining;
drop table if exists "liang-gis-test".public.buildinginfotest;

create table buildinginfotraining (
    id serial primary key,
    EGID TEXT,
    Shape_Area float Default null,
    RoofType TEXT Default null,
    Shape_Length float Default null,
    Border geometry,
    Estimated_Height float Default null
);

CREATE INDEX idx_building_info_traning_border ON buildinginfotraining USING gist (border);

create table "liang-gis-test".public.buildinginfotest (
    id serial primary key,
    EGID TEXT,
    Shape_Area float Default null,
    Altitude_M float Default null,
    RoofType TEXT Default null,
    Shape_Length float Default null,
    Border geometry,
    Estimated_Height float Default null
);

CREATE INDEX idx_building_test_traning_border ON buildinginfotest USING gist (border);

create table "liang-gis-test".public.buildingproto (
    id serial primary key,
    EGID TEXT,
    Border geometry,
);

CREATE INDEX idx_lidar_value_grnd_coord ON lidar_values USING gist (ground_coord);
-- -- Sample points
-- insert into buildingproto (EGID, Border)
-- VALUES (
--     'DC00025306',
--     ST_GeomFromGeoJSON(
--         '{
--             "type": "Multipolygon",
--             "coordinates": [[-77, 38], [-77, 37], [-76, 37], [-76, 38]]
--         }'
--     )
-- );
--
-- insert into buildingproto (EGID, Border)
-- VALUES (
--     'DC00025307',
--     ST_GeomFromGeoJSON(
--         '{
--             "type": "Multipolygon",
--             "coordinates": [[-77, 37], [-77, 36], [-76, 36], [-76, 37]]
--         }'
--     )
-- );
--
-- select * from buildingproto b
-- where ST_Contain(ST_Point( -77.5, 37.5), b.Border)
