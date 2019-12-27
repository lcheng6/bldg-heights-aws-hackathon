FROM amazonlinux:latest
MAINTAINER liangcheng
LABEL Version="0.1"

#COPY ./requirement.txt /root/requirement.txt
RUN yum update -y
RUN yum install python3 -y
RUN pip3 install boto3

COPY ./requirement.txt /root/requirement.txt
RUN pip3 install -r /root/requirement.txt
#RUN pip3 install -r /root/requirement.txt