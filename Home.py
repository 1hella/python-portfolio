import streamlit as st
import pandas
import math

st.set_page_config(layout="wide", page_title="Stephen Wanhella's Portfolio")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpeg", )

with col2:
    st.title("Stephen Wanhella")
    content = """
    Hi, I'm Stephen! I'm a software engineer specializing in Python and Web Development. 
    I graduated from Simon Fraser University in 2021 with a Bachelor of Science in Computer Science.
    I have worked for companies including Elastic Path and LearningBranch (now HiringBranch) on ECommerce and 
    Learning platforms.
    """
    st.info(content)

st.write("Below you can find some of the apps I have built in Python. Feel free to contact me!")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv('data/data.csv', sep=';')

with col3:
    for index, row in df[0:math.ceil(len(df)/2)].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[math.ceil(len(df)/2):].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")