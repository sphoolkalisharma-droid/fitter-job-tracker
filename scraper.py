import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def update_jobs():
    # 2026 की सबसे सटीक सर्च स्ट्रिंग्स
    search_queries = [
        'site:gov.in "fitter" AND "recruitment" after:2026-03-01',
        'site:nic.in "ITI" AND "technician" AND "fitter" 2026',
        'filetype:pdf "fitter" "vacancy" 2026',
        '"NCL" OR "SAIL" OR "RRB" "fitter" recruitment 2026'
    ]
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    all_found = []
    
    for query in search_queries:
        # Google Search (Crawl mode)
        url = f"https://www.google.com/search?q={query}&tbs=qdr:m" # tbs=qdr:m मतलब पिछले 1 महीने का डेटा
        try:
            resp = requests.get(url, headers=headers)
            soup = BeautifulSoup(resp.text, 'html.parser')
            
            for result in soup.select('.tF2Cxc'):
                title = result.select_one('h3').text
                link = result.select_one('a')['href']
                snippet = result.select_one('.VwiC3b').text if result.select_one('.VwiC3b') else ""
                
                # एडवांस फिल्टर: फिटर से जुड़ी जानकारी ही रखें
                if any(word in title.lower() or word in snippet.lower() for word in ["fitter", "technician", "iti"]):
                    all_found.append({
                        "विभाग/संस्था": title[:60] + "...",
                        "स्थिति": "NEW (2026)",
                        "जानकारी": snippet[:100] + "...",
                        "तारीख": datetime.now().strftime("%d-%m-%Y"),
                        "Notification_Link": link,
                        "Apply_Link": link
                    })
        except Exception as e:
            print(f"Error fetching {query}: {e}")
            continue

    if all_found:
        df = pd.DataFrame(all_found).drop_duplicates(subset=['Notification_Link'])
        # सबसे ताजा वैकेंसी ऊपर दिखाएं
        df.to_csv('jobs.csv', index=False)
        print(f"सफलता! {len(df)} ताजा वैकेंसी मिलीं।")
    else:
        print("आज कोई नई वैकेंसी नहीं मिली, पुराने डेटा को सुरक्षित रखा गया है।")

if __name__ == "__main__":
    update_jobs()
