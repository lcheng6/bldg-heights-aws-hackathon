CREATE TABLE building_centroid AS
SELECT b.egid, st_centroid(b.border) as centroid
FROM buildinginfotraining b