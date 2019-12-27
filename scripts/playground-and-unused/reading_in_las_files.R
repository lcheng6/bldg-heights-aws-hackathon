library(rlas)
library(dplyr)
library(sf)
library(httr)

# All the LAS files are downloadable via https
url <- "https://dc-lidar-2018.s3.amazonaws.com/Classified_LAS/1120.las"
GET(url, write_disk("data/r-1120.las", overwrite = T))

# Read in the las file, which by default is a data.table
y = read.las("data/r-1120.las")
# Convert to sf dar-ta frame
y = as_tibble(y) %>% 
    st_as_sf(coords = c("X", "Y")) %>% 
    #explicitly set crs
    st_set_crs(6487)
