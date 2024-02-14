from flask import Flask, request, send_file
from celeryapp import celery_init_app
from tasks import generate_handwriting

from celery.result import AsyncResult


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_mapping(
        CELERY=dict(
            broker_url="redis://localhost",
            result_backend="redis://localhost",
            task_ignore_result=True,
        ),
    )
    app.config.from_prefixed_env()
    celery_init_app(app)
    return app


app = create_app()


@app.post("/")
def start_handwriting():
    text = request.json["text"]
    result = generate_handwriting.delay(text)

    return {"result_id": result.id}


@app.get("/result/<id>")
def task_result(id: str) -> dict[str, object]:
    result = AsyncResult(id)
    return {
        "ready": result.ready(),
        "successful": result.successful(),
        "value": result.result if result.ready() else None,
    }


@app.get("/download/<filename>")
def download_file(filename):
    return send_file(f"file_storage/{filename}.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
