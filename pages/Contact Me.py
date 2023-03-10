import streamlit as st
from send_email import send_email

st.title("Contact Me")

with st.form(key="email_forms"):
    email_address = st.text_input("Your email address")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    if button:
        send_email(email_address, message)
        st.info("Email sent")
