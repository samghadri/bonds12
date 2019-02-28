FROM python:3.6

MAINTAINER Sam Ghadri

ENV PYTHONUNBEFFERED 1
RUN mkdir /flatdocker
WORKDIR /flatdocker

COPY . /flatdocker/

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
