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
