import pathlib
from handwriter import Handwriting

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

pathlib.Path("file_storage").mkdir(exist_ok=True, parents=True)

app = FastAPI()


# Schema
class Text(BaseModel):
    text: list[str]


@app.post("/")
def start_handwriting(data: Text):
    filename = Handwriting(txt=data.text, output_filepath="./file_storage").generate()

    return {"download_link": f"/download/{filename}"}


@app.get("/download/{filename}")
def download_file(filename):
    filepath = pathlib.Path(f"file_storage/{filename}.pdf")

    return FileResponse(filepath, media_type="application/octet-stream")
