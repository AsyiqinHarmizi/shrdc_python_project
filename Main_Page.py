import streamlit as st
import pandas as pd
import plotly.express as px
from googletrans import Translator
import zipfile

# CSS to customize font sizes
st.markdown(
    """
    <style>
    .header-font {
        font-size:35px !important;
        color: #333333;
    }
    .subheader-font {
        font-size:24px !important;
        color: #666666;
    }
    .text-font {
        font-size:18px !important;
        color: #000000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load DataFrame from ZIP file
zip_file_path = "cleaned_dataset.zip"  # Ensure this path is correct

try:
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # List the contents of the ZIP file
        st.write("Contents of the ZIP file:")
        st.write(zip_ref.namelist())

        # Extract a specific file (e.g., 'cleaned_dataset.csv') from the ZIP file
        csv_file_name = 'cleaned_dataset.csv'  # Replace with the actual CSV file name inside the ZIP
        with zip_ref.open(csv_file_name) as file:
            # Read the CSV file into a DataFrame
            df = pd.read_csv(file)
except Exception as e:
    st.error(f"Error reading the ZIP file: {e}")
    st.stop()  # Stop execution if the ZIP file cannot be read

st.header('Geographic Distribution')
st.sidebar.write('Geographic Distribution')

st.info("Description")
st.write("""This website presents an interactive geographic map showcasing the analysis of COVID-19 patient outcomes
          in Mexico for the year 2020. The map visually represents various metrics related to the pandemic,
          allowing users to explore how different regions were affected.
          """)

# Calculate the number of patients (total rows) and deceased patients by country
country_summary = df.groupby('COUNTRY OF ORIGIN').agg(
    Total_Patients=('DATE_OF_DEATH', 'size'),  # Total number of rows (patients) for each country
    Total_Deceased=('DATE_OF_DEATH', lambda x: x.notnull().sum())  # Count of non-null death dates
).reset_index()

# Dropdown to select a specific country or display all
selected_country = st.selectbox("Select a country to highlight (or leave blank to show all):", 
                                ["All"] + country_summary['COUNTRY OF ORIGIN'].unique().tolist())

# Filter the data based on the selected country
if selected_country != "All":
    country_summary_filtered = country_summary[country_summary['COUNTRY OF ORIGIN'] == selected_country]
else:
    country_summary_filtered = country_summary

# Create the choropleth chart
fig = px.choropleth(country_summary_filtered,
                    locations='COUNTRY OF ORIGIN',
                    locationmode='country names',
                    color='Total_Patients',  # Color by total patients
                    hover_name='COUNTRY OF ORIGIN',
                    color_continuous_scale='Viridis',
                    title=f'Total Patients by Country of Origin ({selected_country if selected_country != "All" else "All Countries"})',
                    labels={'Total_Patients': 'Total Patients'})

# Update layout to make the chart larger and customize background
fig.update_layout(
    width=1000,  # Increase the width
    height=700,  # Increase the height
    geo=dict(
        bgcolor='rgba(0,0,0,0)',  # Transparent background
        showland=True,
        landcolor="lightgray",
        showocean=True,
        oceancolor="lightblue",
        projection_type="natural earth",  # Earth-like projection
    )
)
fig.update_geos(fitbounds="locations", visible=False)

# Display the choropleth map
st.header('Total Patients Choropleth Map')
st.plotly_chart(fig)

# Display the country summary values
st.header('Patient Summary by Country')
st.dataframe(country_summary_filtered)
