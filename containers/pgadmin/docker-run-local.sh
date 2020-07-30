#!/bin/bash

#prep the dockermound directory with PGP public keys and other directories

#dockerimage=repo-urbaninst-dev-lidarprocessing

docker pull dpage/pgadmin4
#PGADMIN_DEFAULT_EMAIL required
#PGADMIN_DEFAULT_PASSWORD required
docker run -p 80:80 \
    -e 'PGADMIN_DEFAULT_EMAIL=user@domain.com' \
    -e 'PGADMIN_DEFAULT_PASSWORD=SuperSecret' \
    -d dpage/pgadmin4