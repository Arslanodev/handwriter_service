from celery import shared_task
from handwriter import Handwriting


@shared_task(ignore_result=False)
def generate_handwriting(text: list[str]):
    filename = Handwriting(txt=text, output_filepath="file_storage").generate()

    return {"download_link": f"/download/{filename}"}
