from flask import Flask, render_template, request, send_from_directory
from resume_parser import ResumeParser
from job_matcher import JobMatcher
from section_analyzer import SectionAnalyzer                             
from formatting_checker import FormattingChecker
from report_generator import ReportGenerator
import os

app = Flask(__name__)
UPLOAD_DIR = "uploads"
REPORT_DIR = "reports"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    result = error = report_file = None
    if request.method == "POST":
        resume = request.files.get("resume")
        job = request.files.get("job_description")
        if not resume or not resume.filename:
            error = "Please select a PDF or DOCX resume."
        elif not job or not job.filename:
            error = "Please select a TXT job description."
        else:
            rext = os.path.splitext(resume.filename)[1].lower()
            jext = os.path.splitext(job.filename)[1].lower()
            if rext not in (".pdf", ".docx"):
                error = "Resume must be PDF or DOCX."
            elif jext != ".txt":
                error = "Job description must be TXT."
            else:
                try:
                    rp = os.path.join(UPLOAD_DIR, "resume"+rext)
                    jp = os.path.join(UPLOAD_DIR, "job_description.txt")
                    resume.save(rp); job.save(jp)
                    resume_text = ResumeParser().extract_text(rp)
                    job_text = open(jp, encoding="utf-8", errors="ignore").read()
                    result = {
                        "match_percentage": JobMatcher().match_resume(resume_text, job_text),
                        "sections": SectionAnalyzer().analyze(resume_text),
                        "formatting": FormattingChecker().check(resume_text)
                    }
                    report_file = ReportGenerator().generate_report(result, REPORT_DIR)
                except Exception as e:
                    error = "Could not analyze the files: " + str(e)
    return render_template("index.html", result=result, error=error, report_file=report_file)

@app.route("/download/<path:filename>")
def download(filename):
    return send_from_directory(REPORT_DIR, filename, as_attachment=True)

if __name__ == "__main__":
    app.run("debug run")
