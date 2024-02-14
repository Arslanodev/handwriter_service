from flask import Flask, request, send_file

from handwriter import Handwriting

app = Flask(__name__)


@app.post("/")
def generate_handwriting():
    text = request.json["text"]

    filename = Handwriting(txt=text, output_filepath="file_storage").generate()

    return {"download_link": f"/download/{filename}"}


@app.get("/download/<filename>")
def download_file(filename):
    return send_file(f"file_storage/{filename}.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
