# CREATING MULTIPAGES
import streamlit as st
from PIL import Image
from datetime import datetime

st.image("shrdc_logo.png", width=150)
st.title("COVID-19 in Mexico: A Comprehensive Analysis of Patient Outcomes in 2020")


st.info("Overview of the webpage")
st.write("""Welcome to Our COVID-19 Analysis of Patient Outcomes in Mexico for 2020!

In this webpage, we present an in-depth analysis of COVID-19 patient outcomes in Mexico during year 2020. Dive into our comprehensive dataset to uncover insights and trends that shaped the healthcare landscape during this challenging year.

Explore our interactive charts and detailed analyses, which highlight key findings and provide a clearer understanding of the impact of the pandemic on Mexican patients.

We invite you to:

 - Engage with the data: Navigate through our visualizations to discover patterns and correlations.
 - Learn from our findings: Gain valuable insights into patient demographics, treatment outcomes, and other critical factors.
 - Contribute your thoughts: We encourage feedback and discussions to further enhance our understanding of COVID-19's impact.
         
         """)
st.write("\n")

im = Image.open('covid-header.png')
st.image(im)

st.sidebar.write("""Prepared by:
- Aina
- Asyiqin
- Putri
- Azizah """)
