# Urban

## Infrastructure

> see our infrastructure diagram


## Parsing / Uploading Lidar data

1. Download appropriate `.las` (lidar) data into the data directory.
2. Run `python3 ./lambda/parse-lidar.py data/lidar.las > lidar.sql` to parse the lidar format
3. Upload the lidar.sql to postgres


## Parsing / Uploading Footpring data

1. Download
