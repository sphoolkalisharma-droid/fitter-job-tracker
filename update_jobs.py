import feedparser
import json
import os
from datetime import datetime

# यहाँ ध्यान दें: हर लिंक के बाद " " और अंत में , होना ज़रूरी है
SOURCES = [
    "https://news.google.com/rss/search?q=iti+fitter+govt+jobs+2026&hl=hi&gl=IN&ceid=IN:hi",
    "https://news.google.com/rss/search?q=railway+technician+vacancy+2026&hl=hi&gl=IN&ceid=IN:hi",
    "https://news.google.com/rss/search?q=ncl+singrauli+recruitment+2026&hl=hi&gl=IN&ceid=IN:hi",
    "https://news.google.com/rss/search?q=sail+iti+fitter+jobs&hl=hi&gl=IN&ceid=IN:hi",
    "https://news.google.com/rss/search?q=drdo+fitter+vacancy&hl=hi&gl=IN&ceid=IN:hi"
]

def scrape_all_jobs():
    seen_links = set()
    final_jobs = []
    
    for url in SOURCES:
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries:
                if entry.link not in seen_links:
                    job_data = {
                        "title": entry.title,
                        "link": entry.link,
                        "date": entry.get("published", datetime.now().strftime("%d %b %Y"))
                    }
                    final_jobs.append(job_data)
                    seen_links.add(entry.link)
        except Exception as e:
            print(f"Error: {e}")

    # फाइल सेव करना
    with open("jobs.json", "w", encoding="utf-8") as f:
        json.dump(final_jobs, f, ensure_ascii=False, indent=4)
    
    print(f"Total {len(final_jobs)} jobs found!")

if __name__ == "__main__":
    scrape_all_jobs()
                        
