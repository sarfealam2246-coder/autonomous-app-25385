import streamlit as st
import json

st.set_page_config(page_title="Autonomous App", page_icon="👑", layout="centered")
st.markdown("<style>.stApp { background: #030712; color: #ffffff; }</style>", unsafe_allow_html=True)

st.title("Autonomous App")
st.write("Welcome to your custom application.")
st.info("Goal: [RADAR] 15 AI Super Brain active: Writing code...
[RADAR] GitHub Repository Registered...
[TELEMETRY] GitHub Actions Com")

t_app, t_adm = st.tabs(["📱 User App", "🔐 Owner Admin"])
with t_app:
    phone = st.text_input("Mobile Number (+91):", value="9876543210")
    if st.button("Instant OTP"):
        st.success("Your In-App OTP is: 2246")
    if st.button("Pay via PhonePe (sarfealam@okhdfcbank)"):
        st.success("UPI Intent link active.")
with t_adm:
    pin = st.text_input("Admin PIN", type="password")
    if pin == "2246":
        st.success("Verified Owner: Sarfealam")
        st.write("Banking Destination: sarfealam@okhdfcbank")
