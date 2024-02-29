FROM python:3.12.2-bookworm

WORKDIR /code

ADD ./requirements.txt ./

RUN apt install git \
    && pip3 install -r requirements.txt

COPY ./app ./app

COPY ./file_storage ./