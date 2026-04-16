import feedparser
import json
from datetime import datetime

# 1. सर्च कीवर्ड्स (ताकि ज्यादा से ज्यादा वैकेंसी मिले)
KEYWORDS = ["fitter", "iti fitter", "technician", "railway jobs", "ncl vacancy", "psu jobs"]

# 2. मल्टीपल डेटा सोर्सेज (Google News और Job Feeds)
SOURCES = [
    "https://news.google.com/rss/search?q=iti+fitter+govt+jobs+india&hl=hi&gl=IN&ceid=IN:hi",
    "https://news.google.com/rss/search?q=upcoming+railway+technician+vacancy&hl=hi&gl=IN&ceid=IN:hi",
    "https://www.freejobalert.com/it-jobs/feed/"
]

def fetch_jobs():
    final_job_list = []
    seen_titles = set()

    for url in SOURCES:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            title = entry.title.lower()
            
            # चेक करना कि क्या टाइटल में हमारे काम की चीज है
            if any(key in title for key in KEYWORDS):
                if entry.title not in seen_titles:
                    job_data = {
                        "title": entry.title,
                        "link": entry.link,
                        "date": entry.published if 'published' in entry else str(datetime.now().date())
                    }
                    final_job_list.append(job_data)
                    seen_titles.add(entry.title)

    # 3. डेटा को एक JSON फाइल में सेव करना (जो आपकी वेबसाइट पर दिखेगी)
    with open('jobs.json', 'w', encoding='utf-8') as f:
        json.dump(final_job_list, f, ensure_ascii=False, indent=4)
    
    print(f"Total {len(final_job_list)} vacancies found and updated!")

if __name__ == "__main__":
    fetch_jobs()
