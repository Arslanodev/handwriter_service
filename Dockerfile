FROM python:3.12.0

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

# celery -A tasks worker --loglevel INFO
RUN ["redis-server"]

RUN ["celery", "-A", "app/celeryapp", "worker", "--loglevel INFO"]

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]    