import re
class SectionAnalyzer:
    def analyze(self,text):
        checks={"Contact Information":r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b|(?:\+91[-\s]?)?[6-9]\d{9}",
        "Education":r"\b(education|academic|degree|b\.?tech|bachelor|master|university|college)\b",
        "Skills":r"\b(skills|technical skills|technologies|programming)\b",
        "Experience":r"\b(experience|employment|work history|internship)\b",
        "Projects":r"\b(projects|project experience)\b"}
        return {k:bool(re.search(v,text,re.I)) for k,v in checks.items()}
