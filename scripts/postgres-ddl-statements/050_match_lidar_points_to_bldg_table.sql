-- Update all statistics on all existing tables
vacuum (verbose, analyze) buildinginfotest;
vacuum (verbose, analyze) buildinginfotraining;
vacuum (verbose, analyze) lidar_values;

-- Select the data points from buildinginfotest
create table lidarbuildingmatchtest as
    select bldg.egid as bldg_egid, las.id as las_id
    from buildinginfotest bldg, lidar_values las
    where st_within(las.ground_coord, bldg.border);


-- Select the data points from buildinginfotraining
create table lidarbuildingmatchtraining as
    select bldg.egid as bldg_egid, las.id as las_id
    from buildinginfotraining bldg, lidar_values las
    where st_within(las.ground_coord, bldg.border);

CREATE INDEX if not exists idx_lidarbuildingmatchtest_egid ON lidarbuildingmatchtest USING bldg_egid;
CREATE INDEX if not exists idx_lidarbuildingmatchtraining_egid ON lidarbuildingmatchtraining USING bldg_egid;

vacuum full;