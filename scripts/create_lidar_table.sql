drop table if exists lidar_values;
create table lidar_values
(
    id serial primary key,
    ground_coord geometry,
    -- ground coord is the geo point
    z float not null,
    intensity float not null,
    classification integer not null,
    gps_time float not null,
    overlap float not null,
    scan_angle float not null,
    synthetic integer not null,
    withheld integer not null,
    dcoctocode integer not null
);



-- load some sample values in just to make sure format is correct and then unload the table


truncate lidar_values;

insert into lidar_values (ground_coord, z, intensity, classification, gps_time, overlap, scan_angle, synthetic, withheld, dcoctocode) VALUES
('POINT(-77.12223228002982 38.92961481462707 55.120000000000005)'::geometry, 55.120000000000005, 16750, 2, 207012413.10626054, 1.0, 7.0, 0, 0, 1120),
('POINT(-77.12223965465381 38.92961102341192 55.18)'::geometry, 55.18, 8442.0, 2, 207012413.1062672, 1.0, 7.0, 0, 0, 1120),
('POINT(-77.12224183464343 38.92960444504836 55.26)'::geometry, 55.26, 9112.0, 2, 207012413.1115594, 1.0, 7.0, 0, 0, 1120),
('POINT(-77.1222333076484 38.929608777969214 55.22)'::geometry, 55.22, 10854.0, 2, 207012413.1115663, 1.0, 7.0, 0, 0, 1120),
('POINT(-77.12222501115762 38.929613020564986 55.160000000000004)'::geometry, 55.160000000000004, 20502.0, 2, 207012413.11157322, 1.0, 7.0, 0, 0, 1120),
('POINT(-77.12220425100665 38.929612591864355 55.370000000000005)'::geometry, 55.370000000000005, 27604.0, 2, 207012413.12900543, 1.0, 7.0, 0, 0, 1120),
('POINT(-77.12221208648803 38.92960852991893 55.26)'::geometry, 55.26, 14204.0, 2.0, 207012413.12901235, 1, 7.0, 0, 0, 1120),
('POINT(-77.12221946111244 38.929604738705066 55.300000000000004)'::geometry, 55.300000000000004, 11122.0, 2, 207012413.12901902, 1.0, 7.0, 0, 0, 1120);
