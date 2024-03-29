import os

import pathlib
import uvicorn

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from .worker import celery_app, generate_handwriting

pathlib.Path("file_storage").mkdir(exist_ok=True, parents=True)

app = FastAPI()


# Schema
class Text(BaseModel):
    text: list[str]


@app.post("/")
def start_handwriting(data: Text):
    result = generate_handwriting.delay(data.text)

    return {"result_id": f"/result/{result.id}"}


@app.get("/result/{task_id}")
def task_result(task_id: str) -> dict[str, object]:
    result = celery_app.AsyncResult(task_id)
    return {
        "ready": result.ready(),
        "successful": result.successful(),
        "value": result.result if result.ready() else None,
    }


@app.get("/download/{filename}")
def download_file(filename):
    filepath = pathlib.Path(f"file_storage/{filename}.pdf")
    c1 = os.listdir("file_storage")
    c2 = os.listdir(".")
    c4 = os.listdir("app")
    return c1, c2, c4
    # return FileResponse(filepath, media_type="application/octet-stream")


if __name__ == "__main__":
    uvicorn.run(app)
