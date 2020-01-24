CREATE TABLE building_centroid AS
SELECT b.egid, st_centroid(b.border) as centroid
FROM buildinginfotraining b


--the 2 egid entries should be the same
select c.egid, b.egid
from buildinginfotraining b, building_centroid c
where st_within(c.centroid, b.border)