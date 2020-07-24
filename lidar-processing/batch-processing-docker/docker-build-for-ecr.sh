#!/bin/bash
#this script will build a docker and push it to ECR

export AWS_PROFILE=urban-institute-infranetseccf

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 124836406894.dkr.ecr.us-east-1.amazonaws.com

docker build -t repo-urbaninst-dev-lidarprocessing .

docker tag repo-urbaninst-dev-lidarprocessing:latest 124836406894.dkr.ecr.us-east-1.amazonaws.com/repo-urbaninst-dev-lidarprocessing:latest

docker push 124836406894.dkr.ecr.us-east-1.amazonaws.com/repo-urbaninst-dev-lidarprocessing:latest

unset AWS_PROFILE