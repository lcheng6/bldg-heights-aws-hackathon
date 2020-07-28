create table "lidarbuilding".public.dctracts  (
    id serial primary key,
    STATEFP TEXT,
    COUNTYFP TEXT,
    TRACTCE TEXT,
    GEOID TEXT,
    NAME TEXT,
    NAMELSAD TEXT,
    MTFCC TEXT,
    FUNCSTAT TEXT,
    ALAND float,
    AWATER float,
    INTPTLAT TEXT,
    INTPTLON TEXT,
    Border geometry
);