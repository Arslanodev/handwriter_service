FROM python:3.12.2-bookworm

WORKDIR /code

ADD ./requirements.txt ./

RUN apt install git \
    && pip3 install -r requirements.txt

COPY ./app ./app

EXPOSE 8181

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8181"]