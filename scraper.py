import pandas as pd
from datetime import datetime

def update_jobs():
    # अब इसमें PDF और Direct Apply के कॉलम भी हैं
    job_data = [
        {
            "विभाग": "NCL Singrauli",
            "पद": "Fitter Trainee",
            "अंतिम तिथि": "2026-05-10",
            "PDF नोटिफिकेशन": "https://nclcil.in/recruitment/fitter_notice.pdf",
            "सीधा लिंक (Apply)": "https://www.nclcil.in/apply-online"
        },
        {
            "विभाग": "Railway RRB",
            "पद": "Technician Gr III",
            "अंतिम तिथि": "Upcoming",
            "PDF नोटिफिकेशन": "https://indianrailways.gov.in/notices",
            "सीधा लिंक (Apply)": "https://www.rrbapply.gov.in/"
        },
        {
            "विभाग": "ISRO (VSSC)",
            "पद": "Technician-B",
            "अंतिम तिथि": "2026-04-30",
            "PDF नोटिफिकेशन": "https://www.vssc.gov.in/advt_fitter.pdf",
            "सीधा लिंक (Apply)": "https://imt.vssc.gov.in/apply"
        },
        {
            "विभाग": "BARC",
            "पद": "Stipendiary Trainee",
            "अंतिम तिथि": "Wait",
            "PDF नोटिफिकेशन": "https://barcoc.gov.in/exam_notice",
            "सीधा लिंक (Apply)": "https://barconlineexam.com/"
        }
    ]
    
    df = pd.DataFrame(job_data)
    df.to_csv('jobs.csv', index=False)
    print("Direct Apply Links Updated!")

if __name__ == "__main__":
    update_jobs() 
