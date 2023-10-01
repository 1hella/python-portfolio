import streamlit as st
import pandas
import math

st.set_page_config(layout="wide", page_title="Home • Stephen Wanhella")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", )

with col2:
    st.title("Stephen Wanhella")
    content = """
    Hi, I'm Stephen! I'm a software engineer with an interest in Python. 
    I graduated from Simon Fraser University in 2021 with a Bachelor of Science in Computer Science.
    I have worked for companies including Elastic Path and HiringBranch on ECommerce and 
    Learning platforms. I have experience with Java, JavaScript, Python, and more.
    """
    st.info(content)

st.write("Below you can find some of the projects I have built. Feel free to contact me.")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv('data/data.csv', sep=';')


def get_url_text(url):
    if "github" or "codepen" in url:
        return "Source Code"
    else:
        return "Link"


with col3:
    for index, row in df[0:math.ceil(len(df)/2)].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        url = row['url']
        text = get_url_text(url)
        st.write(f"[{text}]({url})")

with col4:
    for index, row in df[math.ceil(len(df)/2):].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        url = row['url']
        text = get_url_text(url)
        st.write(f"[{text}]({url})")
