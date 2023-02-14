import streamlit as st
import pandas
import math

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Stephen Wanhella")
    content="""
    Hi, I'm Stephen! I'm a software developer specializing in Python and Android Development. 
    I graduated in 2021 with a Bachelor of Science in Computer Science from Simon Fraser University in British Columbia, Canada.
    I have worked with several companies including Elastic Path and HiringBranch (formerly LearningBranch), working on ECommerce and Learning 
    Management solutions.
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