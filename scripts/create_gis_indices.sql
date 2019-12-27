-- run these indices creation for lookup performance improvement

CREATE INDEX idx_building_info_training_border ON buildinginfotraining USING gist (border);
CREATE INDEX idx_building_test_training_border ON buildinginfotest USING gist (border);

CREATE INDEX idx_lidar_value_grnd_coord ON lidar_values USING gist (ground_coord);