import os, pandas as pd
from datetime import datetime
class ReportGenerator:
    def generate_report(self,result,d):
        os.makedirs(d,exist_ok=True)
        fn="ats_report_"+datetime.now().strftime("%Y%m%d_%H%M%S")+".csv"
        rows=[["ATS Match Percentage",result["match_percentage"]["match_percentage"]],
              ["Formatting Score",result["formatting"]["score"]],
              ["Matched Keywords",", ".join(result["match_percentage"]["matched_keywords"])],
              ["Missing Keywords",", ".join(result["match_percentage"]["missing_keywords"])]]
        for k,v in result["sections"].items(): rows.append(["Section - "+k,"Present" if v else "Missing"])
        rows += [["Email Detected","Yes" if result["formatting"]["email"] else "No"],
                 ["Phone Detected","Yes" if result["formatting"]["phone"] else "No"],
                 ["Bullet Points",result["formatting"]["bullets"]],
                 ["Long Lines",result["formatting"]["long_lines"]]]
        pd.DataFrame(rows,columns=["Metric","Result"]).to_csv(os.path.join(d,fn),index=False)
        return fn
