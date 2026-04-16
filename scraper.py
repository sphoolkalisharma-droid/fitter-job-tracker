import pandas as pd
from datetime import datetime

def update_jobs():
    # भारत के सभी मुख्य विभाग (All Departments)
    job_data = [
        # --- महारत्न & नवरत्न PSUs ---
        {"Dept": "PSU-Coal", "Org": "CIL (NCL/WCL/MCL)", "Link": "https://www.coalindia.in/career/"},
        {"Dept": "PSU-Steel", "Org": "SAIL (Bhilai/Bokaro/Rourkela)", "Link": "https://www.sailcareers.com/"},
        {"Dept": "PSU-Power", "Org": "BHEL / NTPC", "Link": "https://careers.bhel.in/"},
        {"Dept": "PSU-Oil", "Org": "IOCL / ONGC / HPCL / BPCL", "Link": "https://iocl.com/latest-job-opening"},
        
        # --- रक्षा & अंतरिक्ष (Defense & Space) ---
        {"Dept": "Defense", "Org": "DRDO / Ordnance Factories", "Link": "https://www.drdo.gov.in/careers"},
        {"Dept": "Space", "Org": "ISRO (VSSC/SDSC/URSC)", "Link": "https://www.isro.gov.in/Careers.html"},
        {"Dept": "Navy/Dock", "Org": "Mazagon Dock / Cochin Shipyard", "Link": "https://mazagondock.in/Career-Online-Recruitment"},
        
        # --- परमाणु ऊर्जा (Atomic Energy) ---
        {"Dept": "Atomic", "Org": "BARC / NPCIL / IGCAR", "Link": "https://npcilcareers.co.in/"},
        
        # --- रेलवे & मेट्रो (Railways) ---
        {"Dept": "Railways", "Org": "RRB Technician / RRC Apprentice", "Link": "https://indianrailways.gov.in/"},
        {"Dept": "Metro", "Org": "DMRC / LMRC / NMRC", "Link": "https://www.delhimetrorail.com/career"},
        
        # --- स्टेट जॉब्स ---
        {"Dept": "State Govt", "Org": "ITI Training Officer (MP/UP/Bihar)", "Link": "https://esb.mp.gov.in/"},
        {"Dept": "State Govt", "Org": "Electricity Board (UPPCL/MPPGCL)", "Link": "https://www.upenergy.in/uppcl/en/page/vacancy-results"}
    ]
    
    df = pd.DataFrame(job_data)
    df['Last_Check'] = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # फाइल सेव करें
    df.to_csv('jobs.csv', index=False)
    print("Mega Department List Updated!")

if __name__ == "__main__":
    update_jobs()
