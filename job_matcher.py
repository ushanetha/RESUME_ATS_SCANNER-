import re
from collections import Counter
STOP={"the","and","for","with","that","this","from","are","you","your","our","will","have","has","job","role","work","using","use","their","can","to","of","in","on","a","an","is","be","as","at","or","we","it","by","must","should"}

class JobMatcher:
    def words(self,text):
        return [w for w in re.findall(r"[a-zA-Z][a-zA-Z0-9+#.-]*",text.lower()) if len(w)>2 and w not in STOP]
    def match_resume(self,resume,job):
        rw=set(self.words(resume)); c=Counter(self.words(job))
        keys=[w for w,_ in c.most_common(30)]
        matched=[w for w in keys if w in rw]
        missing=[w for w in keys if w not in rw]
        pct=round(len(matched)/len(keys)*100,2) if keys else 0
        return {"match_percentage":pct,"matched_keywords":matched,"missing_keywords":missing}
