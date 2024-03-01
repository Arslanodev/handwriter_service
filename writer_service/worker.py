import os

from celery.app import Celery
from handwriter import Handwriting

# Main Celery app
celery_app = Celery(__name__)
celery_app.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://redis:6379/0")
celery_app.conf.result_backend = os.environ.get(
    "CELERY_RESULT_BACKEND", "redis://redis:6379/0"
)
