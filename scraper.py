import pandas as pd

def update_jobs():
    job_data = [
        {
            "विभाग": "NCL Singrauli",
            "पद": "Fitter Trainee",
            "स्थिति": "Active",
            "अंतिम तिथि": "2026-05-10",
            "Notification_Link": "https://nclcil.in/notice.pdf", # असली लिंक डालें
            "Apply_Link": "https://nclcil.in/apply" # असली लिंक डालें
        },
        {
            "विभाग": "Railway RRB",
            "पद": "Technician",
            "स्थिति": "Upcoming",
            "अंतिम तिथि": "जल्द आएगी",
            "Notification_Link": "#", # अभी नहीं है तो # रहने दें
            "Apply_Link": "#" 
        }
    ]
    pd.DataFrame(job_data).to_csv('jobs.csv', index=False)

if __name__ == "__main__":
    update_jobs()
