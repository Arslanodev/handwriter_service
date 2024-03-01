FROM python:3.12.2-bookworm

WORKDIR /celery_worker

COPY ./requirements.txt ./

RUN pip3 install -r requirements.txt

COPY ./app.py ./

CMD ["celery", "-A", "celery_app:app", "worker", "--loglevel=info"]