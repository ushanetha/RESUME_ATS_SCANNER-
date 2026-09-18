# Resume ATS Scanner

A Flask web application that compares a PDF/DOCX resume with a TXT job description and generates an ATS report.

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

## Deploy on Render

1. Push this repository to GitHub.
2. In Render, choose **New > Blueprint** and select this repository, or create a Python web service.
3. Use `pip install -r requirements.txt` as the build command.
4. Use `gunicorn app:app` as the start command.
5. Render will provide the live deployment URL after the service becomes **Live**.

The `/health` endpoint returns HTTP 200 and is used by Render to verify that the service started correctly. Uploaded files and generated reports use `/tmp`, which is appropriate for this stateless demo deployment; generated reports should be downloaded during the same request/session.
