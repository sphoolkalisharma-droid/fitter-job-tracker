import pandas as pd
from datetime import datetime

def update_jobs():
    # यहाँ हम वैकेंसी की पूरी जानकारी मैन्युअली अपडेट कर रहे हैं
    job_data = [
        {
            "विभाग (Dept)": "NCL Singrauli",
            "पद (Post)": "Fitter Trainee",
            "स्थिति (Status)": "LIVE (फॉर्म भरें)",
            "अंतिम तिथि (Last Date)": "2026-05-10",
            "लिंक (Link)": "https://nclcil.in/"
        },
        {
            "विभाग (Dept)": "Railway (RRB)",
            "पद (Post)": "Technician Gr III",
            "स्थिति (Status)": "Upcoming (जल्द आएगी)",
            "अंतिम तिथि (Last Date)": "Wait for Notification",
            "लिंक (Link)": "https://indianrailways.gov.in/"
        },
        {
            "विभाग (Dept)": "BARC",
            "पद (Post)": "Stipendiary Trainee",
            "स्थिति (Status)": "Check Website",
            "अंतिम तिथि (Last Date)": "Coming Soon",
            "लिंक (Link)": "https://barcoc.gov.in/"
        },
        {
            "विभाग (Dept)": "SAIL (Bhilai)",
            "पद (Post)": "ACTT (Fitter)",
            "स्थिति (Status)": "New Notification",
            "अंतिम तिथि (Last Date)": "2026-05-25",
            "लिंक (Link)": "https://www.sailcareers.com/"
        },
        {
            "विभाग (Dept)": "ISRO",
            "पद (Post)": "Technician-B",
            "स्थिति (Status)": "Ongoing",
            "अंतिम तिथि (Last Date)": "2026-04-30",
            "लिंक (Link)": "https://www.isro.gov.in/"
        }
    ]
    
    df = pd.DataFrame(job_data)
    df.to_csv('jobs.csv', index=False)
    print("Full Job Details Updated!")

if __name__ == "__main__":
    update_jobs()
