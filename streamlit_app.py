import streamlit as st
from PIL import Image

# Page config
st.set_page_config(page_title="FutureFit", layout="centered")

# Load and display logo
logo = Image.open("assets/futurefit_logo.png")
st.image(logo, width=250, use_column_width=False)

# Title
st.markdown("<h1 style='text-align: center;'>🎓 FutureFit: College Match for High Schoolers</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter your academic and extracurricular profile to discover your best-fit colleges!</p>", unsafe_allow_html=True)
