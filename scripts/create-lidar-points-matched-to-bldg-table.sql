-- Select the data points from buildinginfotest
create table lidarbuildingmatchtest as
    select bldg.id as bldgid, bldg.egid as egid, bldg.shape_area as shape_area,
           bldg.altitude_m as altitude_m,
           bldg.rooftype as rooftype, bldg.shape_length as shape_length,
           las.z as lidar_z, las.intensity as intensity, las.classification as classification,
           las.gps_time as gps_time, las.overlap as overlap, las.scan_angle as scan_angle,
           las.synthetic as synthetic, las.withheld as withheld, las.dcoctocode as dcoctocode,
           bldg.border as border, las.ground_coord as las_grnd_coord
    from buildinginfotest bldg, lidar_values las
    where st_within(las.ground_coord, bldg.border);


-- Select the data points from buildinginfotraining
create table lidarbuildingmatchtraining as
    select bldg.id as bldgid, bldg.egid as egid, bldg.shape_area as shape_area,
           bldg.rooftype as rooftype, bldg.shape_length as shape_length,
           las.z as lidar_z, las.intensity as intensity, las.classification as classification,
           las.gps_time as gps_time, las.overlap as overlap, las.scan_angle as scan_angle,
           las.synthetic as synthetic, las.withheld as withheld, las.dcoctocode as dcoctocode,
           bldg.border as border, las.ground_coord as las_grnd_coord
    from buildinginfotraining bldg, lidar_values las
    where st_within(las.ground_coord, bldg.border);