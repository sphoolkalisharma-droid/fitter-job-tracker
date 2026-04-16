import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Fitter Job Portal", layout="wide")
st.title("🛠️ ITI Fitter - ऑटोमैटिक जॉब अपडेट")

# डेटा लोड करना
if os.path.exists("jobs.csv"):
    df = pd.read_csv("jobs.csv")
    st.write(f"ताजा अपडेट: {len(df)} नौकरियां मिलीं")
    st.table(df)
else:
    st.warning("अभी डेटा अपडेट हो रहा है... कृपया थोड़ी देर में देखें।")

st.info("यह वेबसाइट रोज़ाना अपने आप अपडेट होती है।")
