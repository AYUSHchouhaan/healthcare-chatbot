import streamlit as st
import pandas as pd
from datetime import datetime

@st.cache_data
def load_data():
    return pd.read_csv(r"medicines_50.csv")

df = load_data()

st.title("💊 Medicine Guidelines & Alternatives")

medicine_name = st.text_input("Enter Medicine Name:", "").strip()

if medicine_name:
    medicine_info = df[df["Medicine Name"].str.contains(medicine_name, case=False, na=False)]

    if not medicine_info.empty:
        medicine_info = medicine_info.iloc[0] 
        
        st.subheader("📝 Medicine Information")
        
        st.subheader("🛠️ Usage")
        st.write(f"**Usage:** {medicine_info['Usage']}")

        expiry_date = datetime.strptime(medicine_info['Expiry Date'], "%Y-%m-%d")
        today = datetime.today()
        
        if expiry_date < today:
            st.error("⚠ This medicine has EXPIRED. Do not use it!")

        st.subheader("🧪 Active Ingredients")
        st.write(f"**Ingredients:** {medicine_info['Active Ingredients']}")

        st.subheader("⚠️ Side Effects")
        st.write(f"**Side Effects:** {medicine_info['Side Effects']}")

        st.subheader("🔄 Alternative Medicine")
        st.write(f"If unavailable, you can use **{medicine_info['Alternatives']}**.")

    else:
        st.warning("⚠ Medicine not found. Please check the spelling.")

