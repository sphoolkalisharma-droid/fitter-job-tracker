import streamlit as st
import pandas as pd

# पेज की सेटिंग
st.set_page_config(page_title="Satyam Fitter Job Tracker", page_icon="🛠️")

# आपकी पहचान (Header)
st.markdown(f"<h1 style='text-align: center; color: #E67E22;'>🛠️ Satyam Sharma (Fitter)</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center;'>ऑल इंडिया सरकारी जॉब ट्रैकर</h3>", unsafe_allow_html=True)
st.write("---")

# मोटिवेशनल लाइन
st.info("🎯 **लक्ष्य:** भारत सरकार के टॉप PSUs और रेलवे में अपनी जगह पक्की करना।")

try:
    df = pd.read_csv('jobs.csv')
    st.success(f"कुल {len(df)} विभागों का डेटा सुरक्षित रूप से ट्रैक हो रहा है।")
    
    # टेबल दिखाना
    st.table(df)
    
    st.markdown("---")
    st.warning("⚠️ **महत्वपूर्ण:** फॉर्म भरने से पहले विभाग की आधिकारिक वेबसाइट पर जाकर पूरा नोटिफिकेशन जरूर पढ़ें।")

except Exception as e:
    st.error("डेटा लोड हो रहा है... कृपया 'Actions' में जाकर एक बार Run Workflow बटन दबाएं।")

# फूटर (Footer)
st.write("---")
st.caption("🚀 यह पोर्टल Satyam Sharma द्वारा अपनी तकनीकी तैयारी और दूसरों की मदद के लिए बनाया गया है।")
