#!/bin/bash

#prep the dockermound directory with PGP public keys and other directories

dockerimage=lastosqltransform
docker stop $(docker ps -a -q)
docker build --tag $dockerimage .

docker run -d -t -i "$dockerimage" /bin/bash
docker exec -it $(docker ps --format "{{.Names}}") /bin/bash