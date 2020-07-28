drop table if exists "liang-gis-test".public.buildinginfotraining;
drop table if exists "liang-gis-test".public.buildinginfotest;

create table buildinginfotraining (
    EGID VARCHAR (12) primary key,
    Shape_Area float Default null,
    RoofType TEXT Default null,
    Shape_Length float Default null,
    Border geometry,
    Estimated_Height float Default null
);

create table "liang-gis-test".public.buildinginfotest (
    EGID VARCHAR (12) primary key,
    Shape_Area float Default null,
    Altitude_M float Default null,
    RoofType TEXT Default null,
    Shape_Length float Default null,
    Border geometry,
    Estimated_Height float Default null
);

CREATE INDEX if not exists idx_building_info_training_border ON buildinginfotraining USING gist (border);
CREATE INDEX if not exists idx_building_test_training_border ON buildinginfotest USING gist (border);