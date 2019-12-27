#!/bin/bash

#prep the dockermound directory with PGP public keys and other directories

dockerimage=lastosqltransform
docker stop $(docker ps -a -q)
docker build --tag $dockerimage .

#extract some environment variables from my own profile to help with docker run
AWS_PROFILE=liangchengkl2_kl2tech

aws_access_key_id=`aws configure get aws_access_key_id`
aws_secret_access_key=`aws configure get aws_secret_access_key`
unset AWS_PROFILE

#load my access credential into the docker's environment variables.
#in real AWS batch run, Boto3 will read directly from the assigned IAM Role
#docker run -d -t -i -e AWS_ACCESS_KEY_ID=$aws_access_key_id -e AWS_SECRET_ACCESS_KEY=$aws_secret_access_key "$dockerimage" --laskey "1120.las"

workingdir=$(pwd)
docker run --mount type=bind,source="${workingdir}/dockermount_tmp",target=/tmp \
  -e AWS_ACCESS_KEY_ID=$aws_access_key_id -e AWS_SECRET_ACCESS_KEY=$aws_secret_access_key "$dockerimage" \
  --memory="2g" --memory-swap="4g" \
  --laskey "1120.las"
