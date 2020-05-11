select bldg.id as bldgid, bldg.egid as egid, bldg.shape_area as shape_area,
       bldg.altitude_m as altitude_m,
       bldg.rooftype as rooftype, bldg.shape_length as shape_length,
       bldg.border as border,
       dc.geoid, dc.name, dc.namelsad
from buildinginfotest bldg, dctracts dc
where st_within(st_centroid(bldg.border), dc.border) and dc.geoid in ('11001005600', '11001010800',  '11001010700', '11001005500');