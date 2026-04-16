import streamlit as st
import pandas as pd
from datetime import datetime

# 1. पेज कॉन्फ़िगरेशन (सबसे एडवांस लुक)
st.set_page_config(
    page_title="SATYAM | FITTER RADAR 2026",
    page_icon="🔥",
    layout="wide"
)

# 2. कस्टम CSS (चमकदार और प्रीमियम लुक के लिए)
st.markdown("""
    <style>
    /* मेन बैकग्राउंड */
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: white;
    }
    /* जॉब कार्ड की स्टाइलिंग */
    .job-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 20px;
        border-left: 5px solid #E67E22;
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
        transition: transform 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .job-card:hover {
        transform: scale(1.02);
        border-left: 5px solid #FF4B2B;
    }
    /* चमकती हुई हेडलाइन */
    .shining-text {
        color: #fff;
        text-align: center;
        font-weight: bold;
        text-transform: uppercase;
        background: linear-gradient(to right, #f39c12 0%, #d35400 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem !important;
        margin-bottom: 0px;
    }
    /* बटन स्टाइलिंग */
    .stButton>button {
        border-radius: 20px;
        background: linear-gradient(45deg, #FF4B2B, #FF416C);
        color: white;
        font-weight: bold;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. वेबसाइट का हेडर
st.markdown("<h1 class='shining-text'>SATYAM SHARMA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2rem; color: #BDC3C7;'>🚀 THE ULTIMATE FITTER JOB RADAR 2026</p>", unsafe_allow_html=True)

# 4. स्टेटस बार
col_a, col_b, col_c = st.columns(3)
with col_a:
    st.metric("टारगेट", "PSU & RAILWAYS")
with col_b:
    st.metric("ट्रेड", "ITI FITTER")
with col_c:
    st.metric("अपडेट", datetime.now().strftime("%d %B"))

st.write("---")

# 5. डेटा लोड करना और दिखाना
try:
    df = pd.read_csv('jobs.csv')
    
    if df.empty:
        st.warning("⚠️ रडार अभी स्कैन कर रहा है... कृपया Actions रन करें।")
    else:
        for _, row in df.iterrows():
            with st.container():
                # कार्ड का ढांचा
                st.markdown(f"""
                <div class="job-card">
                    <h2 style='color: #F1C40F;'>🏢 {row['विभाग/संस्था']}</h2>
                    <p style='font-size: 1.1rem;'><b>🔍 स्थिति:</b> <span style='color: #2ECC71;'>{row['स्थिति']}</span></p>
                    <p style='color: #BDC3C7;'><b>ℹ️ विवरण:</b> {row['जानकारी']}</p>
                    <p style='font-size: 0.9rem; color: #95A5A6;'>📅 रडार पर दिखा: {row['तारीख']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # बटन्स
                c1, c2 = st.columns(2)
                with c1:
                    st.link_button("📄 नोटिफिकेशन डाउनलोड करें", row['Notification_Link'], use_container_width=True)
                with c2:
                    st.link_button("🚀 अभी अप्लाई करें", row['Apply_Link'], type="primary", use_container_width=True)
                st.write("") # स्पेस के लिए

except Exception as e:
    st.error(f"सिस्टम लोड नहीं हुआ। कृपया GitHub पर 'Run Workflow' करें।")

# 6. फुटर
st.markdown("---")
st.markdown("<p style='text-align: center; color: #7F8C8D;'>Designed with Passion by Satyam Sharma | Future PSU Employee</p>", unsafe_allow_html=True)
