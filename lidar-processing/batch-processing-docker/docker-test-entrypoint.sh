#!/bin/bash

#prep the dockermound directory with PGP public keys and other directories

dockerimage=lastosqltransform
docker stop $(docker ps -a -q)
docker build --tag $dockerimage .

docker run $dockerimage hello world