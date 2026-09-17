import re
class FormattingChecker:
    def check(self,text):
        lines=[x.strip() for x in text.splitlines() if x.strip()]
        email=bool(re.search(r"[\w.+-]+@[\w-]+\.[\w.-]+",text))
        phone=bool(re.search(r"(?:\+91[-\s]?)?[6-9]\d{9}",text))
        bullets=sum(bool(re.match(r"^[•●▪◦*-]\s+",x)) for x in lines)
        long_lines=sum(len(x)>150 for x in lines)
        score=round(sum([email,phone,bullets>0,long_lines==0])/4*100,2)
        return {"score":score,"email":email,"phone":phone,"bullets":bullets,"long_lines":long_lines}
