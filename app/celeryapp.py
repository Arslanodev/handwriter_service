from celery.app import Celery
from handwriter import Handwriting

redis_url = "redis://localhost:6379"

celery_app = Celery(__name__, broker=redis_url, backend=redis_url)


@celery_app.task
def generate_handwriting(text: list[str]):
    filename = Handwriting(txt=text, output_filepath="../file_storage").generate()

    return {"download_link": f"/download/{filename}"}
