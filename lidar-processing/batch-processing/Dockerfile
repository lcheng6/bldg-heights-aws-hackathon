FROM amazonlinux:latest
MAINTAINER liangcheng
LABEL Version="0.1"

#COPY ./requirement.txt /root/requirement.txt
RUN yum update -y
RUN yum install python3 -y
RUN pip3 install boto3

COPY ./requirement.txt /root/requirement.txt
RUN pip3 install -r /root/requirement.txt

COPY ./lasutility.py /root/lasutility
COPY ./las-to-sql-processor.py /root/las-to-sql-processor.py
#RUN pip3 install -r /root/requirement.txt
COPY ./entry-point-test.sh /root/entry-point-test.sh

#ENTRYPOINT ["python3", "/root/las-to-sql-processor.py"]
ENTRYPOINT ["/bin/bash", "root/entry-point-test.sh"]