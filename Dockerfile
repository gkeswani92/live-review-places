FROM ubuntu
MAINTAINER Gaurav Keswani <gauravkeswani92@gmail.com>

LABEL Description="This image is used for the Map Nearby Places project"
RUN apt-get update
RUN apt-get install -y git

FROM python:2.7
ENV PYTHONUNBUFFERED 1

RUN mkdir /config
ADD /requirements.txt /config/
RUN pip install -r /config/requirements.txt

RUN mkdir /code;
RUN cd /code

RUN git clone https://github.com/gkeswani92/Map_Nearby_Places.git
WORKDIR Map_Nearby_Places
