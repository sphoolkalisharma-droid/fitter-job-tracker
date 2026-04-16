import pandas as pd
import datetime

# यह ऑटोमैटिक डेटा फाइल बनाने वाला कोड है
jobs = [
    {"Company": "NCL Singrauli", "Post": "Fitter Trainee", "Date": str(datetime.date.today()), "Link": "https://nclcil.in"},
    {"Company": "Railway RRB", "Post": "Technician Gr III", "Date": "Coming Soon", "Link": "https://indianrailways.gov.in"},
    {"Company": "BHEL", "Post": "ITI Fitter Apprentice/Job", "Date": "2026-05-15", "Link": "https://bhel.in"}
]

df = pd.DataFrame(jobs)
df.to_csv("jobs.csv", index=False)
print("Data Updated Successfully!")
