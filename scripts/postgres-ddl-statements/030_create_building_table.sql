drop table if exists "lidarbuilding".public.buildinginfotraining;
drop table if exists "lidarbuilding".public.buildinginfotest;

create table "lidarbuilding".public.buildinginfotraining (
    id serial primary key,
    EGID VARCHAR (12) not null,
    Shape_Area float Default null,
    RoofType TEXT Default null,
    Shape_Length float Default null,
    Border geometry,
    Estimated_Height float Default null
);

create table "lidarbuilding".public.buildinginfotest (
    id serial primary key,
    EGID VARCHAR (12) not null,
    Shape_Area float Default null,
    Altitude_M float Default null,
    RoofType TEXT Default null,
    Shape_Length float Default null,
    Border geometry,
    Estimated_Height float Default null
);

CREATE INDEX if not exists idx_building_info_training_border ON buildinginfotraining USING gist (border);
CREATE INDEX if not exists idx_building_test_training_border ON buildinginfotest USING gist (border);