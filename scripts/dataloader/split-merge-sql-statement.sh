#!/bin/bash -xe

orig_sql_file=$1

pushd .
cd splitsql

split -l 500000 /tmp/$orig_sql_file

first_string='insert into lidar_values (ground_coord, z, intensity, classification, gps_time, overlap, scan_angle, synthetic, withheld, dcoctocode) VALUES'

for f in x*; do 
	echo "File -> $f"
	if [ $f != 'xaa' ]; then 
		sed -i "1i${first_string}" $f 
	fi
	sed -i '$ s/,$/;/' ${f} 
done

cat x* > /tmp/$orig_sql_file

rm *

popd

