#!/bin/bash
#this script will build a docker and push it to ECR

AWS_PROFILE=liangchengkl2_kl2tech

$(aws ecr get-login --no-include-email --region us-east-1)
docker build -t lastosqltransform .

docker tag lastosqltransform:latest 931047198824.dkr.ecr.us-east-1.amazonaws.com/lastosqltransform:latest

docker push 931047198824.dkr.ecr.us-east-1.amazonaws.com/lastosqltransform:latest

unset AWS_PROFILE