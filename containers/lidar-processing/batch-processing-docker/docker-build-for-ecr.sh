#!/bin/bash
#this script will build a docker and push it to ECR

dockerimage=repo-urbaninst-dev-lidarprocessing
export AWS_PROFILE=urban-institute-infranetseccf

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 124836406894.dkr.ecr.us-east-1.amazonaws.com

docker build -t ${dockerimage} .

docker tag ${dockerimage}:latest 124836406894.dkr.ecr.us-east-1.amazonaws.com/repo-urbaninst-dev-lidarprocessing:latest

docker push 124836406894.dkr.ecr.us-east-1.amazonaws.com/${dockerimage}:latest

unset AWS_PROFILE