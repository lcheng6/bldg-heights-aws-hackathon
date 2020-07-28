-- run these indices creation for lookup performance improvement

CREATE INDEX if not exists idx_building_info_training_border ON buildinginfotraining USING gist (border);
CREATE INDEX if not exists idx_building_test_training_border ON buildinginfotest USING gist (border);
CREATE INDEX if not exists idx_lidar_value_grnd_coord ON lidar_values USING gist (ground_coord);


-- run these indices to help with building information lookup

CREATE INDEX if not exists idx_lidarbuildingmatchtest_bldgid ON lidarbuildingmatchtest (bldgid);
-- CREATE INDEX if not exists idx_lidarbuildingmatchtraining_bldgid ON lidarbuildingmatchtraining (bldgid);

-- activate all index and improve search performance
REINDEX DATABASE lidarbuilding