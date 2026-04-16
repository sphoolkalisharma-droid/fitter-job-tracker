import feedparser
import json
import os
from datetime import datetime

# महा-सोर्स लिस्ट: इसमें हमने सब कुछ कवर कर लिया है
SOURCES = [
    # PSU और सरकारी नौकरी के कीवर्ड्स
    "https://news.google.com/rss/search?q=latest+PSU+jobs+recruitment+2026&hl=hi&gl=IN&ceid=IN:hi",
    "https://news.google.com/rss/search?q=Railway+Technician+RRB+recruitment+2026&hl=hi&gl=IN&ceid=IN:hi",
    "https://news.google.com/rss/search?q=ITI+Fitter+Govt+Jobs+Vacancy&hl=hi&gl=IN&ceid=IN:hi",
    "https://news.google.com/rss/search?q=NCL+Singrauli+NTPC+SAIL+GAIL+jobs&hl=hi&gl=IN&ceid=IN:hi",
    "https://news.google.com/rss/search?q=Central+Govt+Jobs+for+ITI+holders&hl=hi&gl=IN&ceid=IN:hi",
    "https://www.freejobalert.com/it-jobs/feed/",
    "https://www.fresherslive.com/it-jobs/rss-feed"
]

def scrape_all_jobs():
    seen_links = set()
    final_jobs = []
    
    print("Searching for unlimited vacancies...")
    
    for url in SOURCES:
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries:
                # डुप्लीकेट रोकने के लिए
                if entry.link not in seen_links:
                    job_data = {
                        "title": entry.title,
                        "link": entry.link,
                        "date": entry.get("published", datetime.now().strftime("%d %b %Y")),
                        "source": "Official Update"
                    }
                    final_jobs.append(job_data)
                    seen_links.add(entry.link)
        except Exception as e:
            print(f"Error checking source: {e}")

    # jobs.json में डेटा लिखना (Main Directory वाली फाइल)
    with open("jobs.json", "w", encoding="utf-8") as f:
        json.dump(final_jobs, f, ensure_ascii=False, indent=4)
    
    print(f"Total {len(final_jobs)} jobs found and updated!")

if __name__ == "__main__":
    scrape_all_jobs()
                        
