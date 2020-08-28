drop table if exists "lidarbuilding".public.ms_building_borders;

create table "lidarbuilding".public.ms_building_borders (
    id serial primary key,
    State VARCHAR (64) not null,
    Border geometry,
    BorderCentroid geometry
);