create table building_detailed_info_within_ajjits_selected_tracts as
    select bldg.id as bldgid, bldg.egid as egid, bldg.shape_area as shape_area,
           bldg.altitude_m as altitude_m,
           bldg.rooftype as rooftype, bldg.shape_length as shape_length,
           bldg.border as border,
           dc.geoid, dc.name, dc.namelsad
    from buildinginfotest bldg, dctracts dc
    where st_within(st_centroid(bldg.border), dc.border) and dc.geoid in ('11001005600', '11001010800',  '11001010700', '11001005500');
ALTER TABLE "building_detailed_info_within_ajjits_selected_tracts" ADD PRIMARY KEY (bldgid);
ALTER TABLE "building_detailed_info_within_ajjits_selected_tracts"
ADD COLUMN pct999 float,
ADD COLUMN pct995 float,
ADD COLUMN pct990 float,
ADD COLUMN pct950 float;

