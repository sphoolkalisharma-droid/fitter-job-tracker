import json, datetime, random

def update():
    try:
        with open('questions.json', 'r', encoding='utf-8') as f: data = json.load(f)
    except: data = {"pyq":[], "ai_daily_sets":[], "dictionary":[]}
    
    today = datetime.datetime.now().strftime("%d %B %Y")
    if any(s['set_date'] == today for s in data['ai_daily_sets']): return

    # यहाँ आप नए सवाल जोड़ सकते हैं
    new_q = [
        {"q": "लेथ बेड किस मटेरियल का बना होता है?", "a": "Cast Iron"},
        {"q": "V-Block का एंगल कितना होता है?", "a": "90 Degree"}
    ]
    data['ai_daily_sets'].append({"set_date": today, "questions": new_q})
    if len(data['ai_daily_sets']) > 5: data['ai_daily_sets'].pop(0)

    with open('questions.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__": update()
