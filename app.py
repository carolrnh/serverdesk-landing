import os
from flask import Flask, send_from_directory

app = Flask(__name__)
ROOT = os.path.dirname(os.path.abspath(__file__))

@app.get("/")
def index():
    return send_from_directory(ROOT, "index.html")

@app.get("/styles.css")
def css():
    return send_from_directory(ROOT, "styles.css")

@app.get("/images/<path:filename>")
def images(filename):
    return send_from_directory(os.path.join(ROOT, "images"), filename)

@app.get("/privacy")
def privacy():
    return send_from_directory(ROOT, "privacy.html")

@app.get("/privacy.html")
def privacy_html():
    return send_from_directory(ROOT, "privacy.html")

@app.get("/terms")
def terms():
    return send_from_directory(ROOT, "terms.html")

@app.get("/terms.html")
def terms_html():
    return send_from_directory(ROOT, "terms.html")


@app.get("/setup")
def setup():
    return send_from_directory(ROOT, "setup.html")

@app.get("/setup.html")
def setup_html():
    return send_from_directory(ROOT, "setup.html")

@app.get("/health")
def health():
    return {"ok": True}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8788")))
