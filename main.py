import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpeg")

with col2:
    st.title("Stephen Wanhella")
    content="""
    Hi, I'm Stephen! I'm a software developer specializing in Python and Android Development. 
    I graduated in 2021 with a Bachelor of Science in Computer Science from Simon Fraser University in British Columbia, Canada.
    I have worked with several companies including Elastic Path and HiringBranch (formerly LearningBranch), working on ECommerce and Learning 
    Management solutions.
    """
    st.info(content)