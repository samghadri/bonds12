FROM python:3.6

ENV PYTHONUNBEFFERED 1
RUN mkdir /code
WORKDIR /flatdocker


COPY . /flatdocker/

RUN pip install -r requirements.txt
