INSERT INTO lidar_values (X, Y, Z, intensity, classification, gps_time, overlap, scan_angle) VALUES
(38940126.0, 14019987.0, 5512.0, 16750.0, 2.0, 207012413.10626054, 1.0, 7.0),(38940062.0, 14019945.0, 5518.0, 8442.0, 2.0, 207012413.1062672, 1.0, 7.0)

create table lidar_values
(
    id serial primary key,
    ground_coord geometry,
    -- ground coord is the geo point
    z float not null,
    intensity float not null,
    classification float not null,
    gps_time float not null,
    overlap float not null,
    scan_angle float not null
);

--    80.41027603367428 -71.46076782128519 5577
insert into lidar_values (ground_coord, z, intensity, classification, gps_time, overlap, scan_angle)
(
    ST_SetSRID(ST_MakePoint(80.41027603367428 -71.46076782128519 5577), 4326),
    5512.0, 16750.0, 2.0, 207012413.10626054, 1.0, 7.0
)