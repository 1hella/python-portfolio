import streamlit as st

from send_email import send_email

st.set_page_config(page_title="Contact Me • Stephen Wanhella")

st.title("Contact Me")
with st.form(key="email_forms", clear_on_submit=True):
    if 'submitted' not in st.session_state:
        st.session_state['submitted'] = False

    name = st.text_input("Your name", key="name",
                         value=st.session_state['name'] if 'name' in st.session_state and not st.session_state[
                             'submitted'] else '')
    name_error_message = st.empty()
    email_address = st.text_input("Your email address", key="email",
                                  value=st.session_state['email'] if "email" in st.session_state and not
                                  st.session_state['submitted']
                                  else "")
    email_error_message = st.empty()
    message = st.text_area("Your message", key="message",
                           value=st.session_state['message'] if "message" in st.session_state and not st.session_state[
                               'submitted'] else "")
    message_error_message = st.empty()
    submit = st.form_submit_button("Submit")
    if st.session_state['submitted']:
        st.info("Email sent")
        st.session_state['submitted'] = False
    if submit:
        error = False
        if name == "":
            name_error_message.error("Please enter your name")
            error = True
        if email_address == "":
            email_error_message.error("Please enter your email address")
            error = True
        if message == "":
            message_error_message.error("Please enter your message")
            error = True
        if not error:
            send_email(email_address, message, name)
            st.session_state['submitted'] = True
            st.experimental_rerun()
        else:
            st.session_state['submitted'] = False
