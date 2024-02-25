import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS
lottie_coding = load_lottieurl("https://lottie.host/7480ae41-f96f-4cd6-a7ba-8b243288bf31/8FwbyQWR0b.json")


col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    # ---- HEADER SECTION
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader("Hi, I am Christopher :wave:")
            st.title("A Computer Systems Engineering Graduate from Fiji")
            st.write(
                "I am currently seeking out graduate and internship opportunities to improve upon my technical skillset, "
                "whilst in a professional environment.")
            st.write("[LinkedIn >](https://www.linkedin.com/in/christopher-kumar-26b5792b1/)")
            st.write("[GitHub >](https://github.com/christopherkumar)")
            st.write("[Instagram >](https://www.instagram.com/christopherkumar812/)")
        with right_column:
            st.image(Image.open('images/dp.png'), width=300)

    # ---- ABOUT ME
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("About me")
            st.write("As an aspiring Computer Systems Engineering professional, I am in the final stages of earning my "
                     "Bachelor of Engineering (Honours) at the University of Southern Queensland. My academic and "
                     "professional journey is marked by a blend of technical proficiency, practical experience, "
                     "and community engagement.")
            st.subheader("Academic background")
            st.write("University of Southern Queensland: Bachelor of Engineering (Honours)"
                     " - Computer Systems Engineering. ")
            st.write("University of the South Pacific - Foundation Science Programme.")
        with right_column:
            st_lottie(lottie_coding, width=300, key="coding")

    # ---- EXPERIENCE
    with st.container():
        st.write("---")
        st.subheader("Professional experience")
        st.write("- Data Labelling for Machine Vision Projects: Contributed as a contract worker at the Centre for "
                 "Agricultural Engineering, University of Southern Queensland, enhancing machine vision technologies "
                 "through meticulous data labeling.")
        st.write("- Cafe and Barista Experience: Gained valuable customer service and operational management skills "
                 "working at the Bounce Hub Cafe.")
        st.subheader("Volunteer experience")
        st.write("- Vinnies SENSE: Demonstrated a commitment to community service by volunteering, showcasing my "
                 "dedication to contributing positively to society.")
        st.subheader("Technical skills")
        st.write("- Programming Proficiency: Skilled in MATLAB, C++/C, and Python, with foundational knowledge in "
                 "Arduino and AutoCAD.")
        st.write("- Software Expertise: Proficient with the Microsoft Office Suite, emphasizing my versatility in "
                 "technical and administrative tasks.")

    # ---- PROJECTS
    with st.container():
        st.write("---")
        st.subheader("Personal projects")
        st.write("- Undergraduate Research Project: Investigated the effects of camera models and settings on image "
                 "classification accuracy, utilizing PyTorch, Python, and MATLAB.")
        st.write("- Development Projects: Created a personal links dashboard and a webpage using Python and Streamlit.")
