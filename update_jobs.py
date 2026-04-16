import feedparser
import json
import os

# ज्यादा वैकेंसी के लिए नए सोर्सेज
SOURCES = [
    "https://news.google.com/rss/search?q=iti+fitter+govt+jobs+2026&hl=hi&gl=IN&ceid=IN:hi",
    "https://news.google.com/rss/search?q=railway+technician+vacancy+2026&hl=hi&gl=IN&ceid=IN:hi",
    "https://news.google.com/rss/search?q=ncl+singrauli+recruitment+2026&hl=hi&gl=IN&ceid=IN:hi",
    "https://news.google.com/rss/search?q=sail+iti+fitter+jobs&hl=hi&gl=IN&ceid=IN:hi",
    "https://news.google.com/rss/search?q=drdo+fitter+vacancy&hl=hi&gl=IN&ceid=IN:hi"
]

def scrape_jobs():
    all_jobs = []
    for url in SOURCES:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            job = {
                "title": entry.title,
                "link": entry.link,
                "date": entry.published
            }
            all_jobs.append(job)
    
    # सिर्फ टॉप 20 वैकेंसी सेव करें
    with open("jobs.json", "w", encoding="utf-8") as f:
        json.dump(all_jobs[:20], f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    scrape_jobs()
    print("Vancancy updated successfully!")
