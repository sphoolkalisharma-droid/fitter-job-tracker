import streamlit as st
import pandas as pd
import os

# पेज की सेटिंग
st.set_page_config(page_title="Satyam Fitter Job Radar", layout="wide")

st.title("Satyendra Bhaiya & Satyam Sharma - Fitter Job Radar 2026")
st.write("🚀 ITI FITTER | PSU | RAILWAYS | LATEST UPDATES")

# डेटा लोड करने का फंक्शन
def load_data():
    if os.path.exists('jobs.csv'):
        df = pd.read_csv('jobs.csv')
        return df
    else:
        return None

data = load_data()

if data is not None and not data.empty:
    st.success(f"कुल {len(data)} नई नौकरियां मिली हैं!")
    # टेबल के रूप में डेटा दिखाना
    st.dataframe(data, use_container_width=True)
else:
    st.warning("अभी डेटा लोड हो रहा है... कृपया GitHub Actions में 'Run Workflow' चेक करें।")

st.markdown("---")
st.info("Designed with Passion for Fitter Aspirants")
