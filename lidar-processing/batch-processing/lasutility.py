import numpy as np
from laspy.file import File
from pandas import DataFrame
from geopandas import GeoDataFrame
from shapely.geometry import Point
import requests
import os

def get_las_file_names():
    
    #for convenience's sake just listing all the las files within s3://dc-lidar-2018/Classified_LAS/ folder
    return [
        "1120.las",
        "1121.las",
        "1122.las",
        "1218.las",
        "1219.las",
        "1220.las",
        "1221.las",
        "1222.las",
        "1223.las",
        "1317.las",
        "1318.las",
        "1319.las",
        "1320.las",
        "1321.las",
        "1322.las",
        "1323.las",
        "1324.las",
        "1417.las",
        "1418.las",
        "1419.las",
        "1420.las",
        "1421.las",
        "1422.las",
        "1423.las",
        "1424.las",
        "1425.las",
        "1517.las",
        "1518.las",
        "1519.las",
        "1520.las",
        "1521.las",
        "1522.las",
        "1523.las",
        "1524.las",
        "1525.las",
        "1526.las",
        "1616.las",
        "1617.las",
        "1618.las",
        "1619.las",
        "1620.las",
        "1621.las",
        "1622.las",
        "1623.las",
        "1624.las",
        "1625.las",
        "1626.las",
        "1627.las",
        "1714.las",
        "1715.las",
        "1716.las",
        "1717.las",
        "1718.las",
        "1719.las",
        "1720.las",
        "1721.las",
        "1722.las",
        "1723.las",
        "1724.las",
        "1725.las",
        "1726.las",
        "1727.las",
        "1728.las",
        "1812.las",
        "1813.las",
        "1814.las",
        "1815.las",
        "1816.las",
        "1817.las",
        "1818.las",
        "1819.las",
        "1820.las",
        "1821.las",
        "1822.las",
        "1823.las",
        "1824.las",
        "1825.las",
        "1826.las",
        "1827.las",
        "1828.las",
        "1829.las",
        "1907.las",
        "1908.las",
        "1911.las",
        "1912.las",
        "1913.las",
        "1914.las",
        "1915.las",
        "1916.las",
        "1917.las",
        "1918.las",
        "1919.las",
        "1920.las",
        "1921.las",
        "1922.las",
        "1923.las",
        "1924.las",
        "1925.las",
        "1926.las",
        "1927.las",
        "1928.las",
        "1929.las",
        "1930.las",
        "2001.las",
        "2002.las",
        "2003.las",
        "2004.las",
        "2005.las",
        "2006.las",
        "2007.las",
        "2008.las",
        "2009.las",
        "2010.las",
        "2011.las",
        "2012.las",
        "2013.las",
        "2014.las",
        "2015.las",
        "2016.las",
        "2017.las",
        "2018.las",
        "2019.las",
        "2020.las",
        "2021.las",
        "2022.las",
        "2023.las",
        "2024.las",
        "2025.las",
        "2026.las",
        "2027.las",
        "2028.las",
        "2029.las",
        "2102.las",
        "2103.las",
        "2104.las",
        "2105.las",
        "2106.las",
        "2107.las",
        "2108.las",
        "2109.las",
        "2110.las",
        "2111.las",
        "2112.las",
        "2113.las",
        "2114.las",
        "2115.las",
        "2116.las",
        "2117.las",
        "2118.las",
        "2119.las",
        "2120.las",
        "2121.las",
        "2122.las",
        "2123.las",
        "2124.las",
        "2125.las",
        "2126.las",
        "2127.las",
        "2128.las",
        "2203.las",
        "2204.las",
        "2205.las",
        "2206.las",
        "2207.las",
        "2208.las",
        "2209.las",
        "2210.las",
        "2211.las",
        "2212.las",
        "2213.las",
        "2214.las",
        "2215.las",
        "2216.las",
        "2217.las",
        "2218.las",
        "2219.las",
        "2220.las",
        "2221.las",
        "2222.las",
        "2223.las",
        "2224.las",
        "2225.las",
        "2226.las",
        "2227.las",
        "2304.las",
        "2305.las",
        "2306.las",
        "2307.las",
        "2308.las",
        "2309.las",
        "2310.las",
        "2311.las",
        "2312.las",
        "2313.las",
        "2314.las",
        "2315.las",
        "2316.las",
        "2317.las",
        "2318.las",
        "2319.las",
        "2320.las",
        "2321.las",
        "2322.las",
        "2323.las",
        "2324.las",
        "2325.las",
        "2326.las",
        "2405.las",
        "2406.las",
        "2407.las",
        "2408.las",
        "2409.las",
        "2410.las",
        "2411.las",
        "2412.las",
        "2413.las",
        "2414.las",
        "2415.las",
        "2416.las",
        "2417.las",
        "2418.las",
        "2419.las",
        "2420.las",
        "2421.las",
        "2422.las",
        "2423.las",
        "2424.las",
        "2425.las",
        "2506.las",
        "2507.las",
        "2508.las",
        "2509.las",
        "2510.las",
        "2511.las",
        "2512.las",
        "2513.las",
        "2514.las",
        "2515.las",
        "2516.las",
        "2517.las",
        "2518.las",
        "2519.las",
        "2520.las",
        "2521.las",
        "2522.las",
        "2523.las",
        "2524.las",
        "2607.las",
        "2608.las",
        "2609.las",
        "2610.las",
        "2611.las",
        "2612.las",
        "2613.las",
        "2614.las",
        "2615.las",
        "2616.las",
        "2617.las",
        "2618.las",
        "2619.las",
        "2620.las",
        "2621.las",
        "2622.las",
        "2623.las",
        "2708.las",
        "2709.las",
        "2710.las",
        "2711.las",
        "2712.las",
        "2713.las",
        "2714.las",
        "2715.las",
        "2716.las",
        "2717.las",
        "2718.las",
        "2719.las",
        "2720.las",
        "2721.las",
        "2722.las",
        "2809.las",
        "2810.las",
        "2811.las",
        "2812.las",
        "2813.las",
        "2814.las",
        "2815.las",
        "2816.las",
        "2817.las",
        "2818.las",
        "2819.las",
        "2820.las",
        "2821.las",
        "2910.las",
        "2911.las",
        "2912.las",
        "2913.las",
        "2914.las",
        "2915.las",
        "2916.las",
        "2917.las",
        "2918.las",
        "2919.las",
        "2920.las",
        "3011.las",
        "3012.las",
        "3013.las",
        "3014.las",
        "3015.las",
        "3016.las",
        "3017.las",
        "3018.las",
        "3019.las",
        "3112.las",
        "3113.las",
        "3114.las",
        "3115.las",
        "3116.las",
        "3117.las",
        "3118.las",
        "3213.las",
        "3214.las",
        "3215.las",
        "3216.las",
        "3217.las",
        "3314.las",
        "3315.las",
        "3316.las",
        "3415.las"
    ];

def get_s3_path_from_keyname(keyname):
    return f"s3://dc-lidar-2018/Classified_LAS/{keyname}"

def https_path_from_keyname(keyname):
    return f"https://s3.amazonaws.com/dc-lidar-2018/Classified_LAS/{keyname}"

def download_las_data(keyname):
    url = lasutility.https_path_from_keyname(keyname)
    lidar_data = requests.get(url)
    lasdatafile = f"./lasdata/{keyname}"
    with open(lasdatafile, "wb+") as f:
        f.write(lidar_data.content)

def cleanup_las_data(keyname):
    lasdatafile = f"./lasdata/{keyname}"
    os.remove(lasdatafile)

def convert_las_data_to_sql_statement(keyname, max_rows_per_iteration = 10000):
    #we need to partition the GeoDataFrame.to_crs function to 10,000 blocks, otherwise jupyter seem to have memory errors
    #might need to come back to this and recheck
    lasdatafile = f"./lasdata/{keyname}"
    keysequencenum = keyname.split('.')[0] #get the #### of the file "####.las"
    lassqlfile = f"./lasdata/{keysequencenum}.sql"
    inFile = File(lasdatafile)
    row_count = 0
    lidar_points = np.array((inFile.X,inFile.Y,inFile.Z,inFile.intensity,
                             inFile.classification, inFile.gps_time,
                             inFile.overlap, inFile.scan_angle,
                             inFile.x, inFile.y, inFile.z,
                             inFile.Synthetic, inFile.Withheld)).transpose()
    lidar_df=DataFrame(lidar_points, columns = ["X","Y","Z","intensity",
                                                "classification","gps_time",
                                                "overlap","scan_angle",
                                                "x", "y", "z",
                                                "synthentic", "withheld"])

    lidar_df_total_length = lidar_df.shape[0]
    sql_lines_array = []
    sql_preamble = f"insert into lidar_values (ground_coord, z, intensity, classification, gps_time, overlap, scan_angle, synthetic, withheld, dcoctocode) VALUES"

    sql_lines_array.append(sql_preamble)
    for lidar_idx_start in range(0, lidar_df_total_length, max_rows_per_iteration):
        lidar_idx_end = lidar_idx_start + max_rows_per_iteration
        lidar_idx_end = min(lidar_idx_end, lidar_df_total_length)
        lidar_indices_curr_iter = np.arange(lidar_idx_start, lidar_idx_end)
        lidar_df_sampled = lidar_df.iloc[lidar_indices_curr_iter]

        geometry_sampled = [Point(xyz) for xyz in zip(lidar_df_sampled.x,lidar_df_sampled.y,lidar_df_sampled.z)]

        crs = None
        lidar_geodf_sampled = GeoDataFrame(lidar_df_sampled, crs=crs, geometry=geometry_sampled)
        lidar_geodf_sampled.crs = {'init': 'epsg:26985'}
        lidar_geodf_sampled['geometry'] = lidar_geodf_sampled['geometry'].to_crs(epsg=4326)

        for idx, frame in lidar_geodf_sampled.iterrows():
            row_count+=1
            X, Y, Z, intensity, classification, gps_time, overlap, scan_angle, x, y, z, synthetic, withheld, geom = frame.to_list()
            lat, long, z = geom.x, geom.y, geom.z #  Replace the old CRS values and move this over.
            items = [f"'POINT({lat} {long} {z})'::geometry", z, intensity, classification, gps_time, overlap, scan_angle, synthetic, withheld, keysequencenum]
            items_str = map(str, items)
            sql_line = ', '.join(items_str)
            sql_lines_array.append(sql_line);


    sql_complete_statement = ",\n".join(sql_lines_array)
    text_file = open(lassqlfile, "w")
    text_file.write(sql_complete_statement)
    text_file.close()

    return row_count # return the number of entries created

def upload_las_data_to_s3_bucket(keyname, s3bucket, s3prefix):
    s3_client = boto3.client('s3')
    local_path = f"./lasdata/{keyname}"
    object_name = f"{s3prefix}/{keyname}"
    try:
        response = s3_client.upload_file(local_path, s3bucket, object_name)
    except ClientError as e:
        return False
    return True