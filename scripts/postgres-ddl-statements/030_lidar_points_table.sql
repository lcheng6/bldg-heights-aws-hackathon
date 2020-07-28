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
CREATE INDEX if not exists idx_lidar_value_grnd_coord ON lidar_values USING gist (ground_coord);