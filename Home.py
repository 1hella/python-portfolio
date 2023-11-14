import math
import os

import pandas
import streamlit as st
import streamlit_analytics
from dotenv import load_dotenv
from config_manager import ConfigManager

from url_to_link import get_url_text

st.set_page_config(layout="wide", page_title="Home • Stephen Wanhella")

load_dotenv()
config_file = ConfigManager.get_config_file()
with streamlit_analytics.track(unsafe_password=os.getenv('STREAMLIT_PASSWORD'),
                               firestore_key_file=config_file, firestore_collection_name="home"):
    col1, col2 = st.columns(2)

    with col1:
        st.image("images/photo.jpg", )

    with col2:
        st.title("Stephen Wanhella")
        content = """
        Hi, I'm Stephen! I'm a software engineer/tester. 
        I have worked for Elastic Path and HiringBranch on ECommerce and 
        Learning platforms. I work with Java, JavaScript, SQL, Selenium, and much more.
        I graduated from Simon Fraser University in British Columbia in 2021 with a Bachelor of Science in Computer Science.
        I'm available for hire.
        """
        st.info(content)

    st.write("Below you can find some of the projects I have built. Feel free to contact me.")

    col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

    df = pandas.read_csv('data/data.csv', sep=';')

    with col3:
        for index, row in df[0:math.ceil(len(df) / 2)].iterrows():
            st.header(row['title'])
            st.write(row['description'])
            st.image('images/' + row['image'])
            url = row['url']
            text = get_url_text(url)
            st.write(f"[{text}]({url})")

    with col4:
        for index, row in df[math.ceil(len(df) / 2):].iterrows():
            st.header(row['title'])
            st.write(row['description'])
            st.image('images/' + row['image'])
            url = row['url']
            text = get_url_text(url)
            st.write(f"[{text}]({url})")

    st.write("[Contact Me](./Contact_Me)")
