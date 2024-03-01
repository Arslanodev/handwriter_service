from celery import Celery
from handwriter import Handwriting

app = Celery(__name__)
app.conf.broker_url = "redis://redis:6769/0"
app.conf.result_backend = "redis://redis:6769/0"


@app.task()
def generate_handwriting(text: list[str]):
    filename = Handwriting(txt=text, output_filepath="./file_storage").generate()

    return {"download_link": f"/download/{filename}"}
