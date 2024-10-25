import streamlit as st
import pandas as pd
import plotly.express as px
from googletrans import Translator

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
    unsafe_allow_html=True)

# Example DataFrame
df = pd.read_csv("dataset.csv")

#Data Transformation
df["SEX"] = df["SEX"].map({1:"FEMALE", 2:"MALE", 99:"UNKNOWN"})
df["HOSPITALIZED"] = df["HOSPITALIZED"].map({1:"NO", 2:"YES", 99:"UNKNOWN"})
df["INTUBATED"] = df["INTUBATED"].map({1:"YES", 2:"NO",97:"DOES NOT APPLY",98:"IGNORED", 99:"UNKNOWN"})
df["PNEUMONIA"] = df["PNEUMONIA"].map({1:"YES", 2:"NO",97:"DOES NOT APPLY",98:"IGNORED", 99:"UNKNOWN"})
df["PREGNANCY"] = df["PREGNANCY"].map({1:"YES", 2:"NO",97:"DOES NOT APPLY",98:"IGNORED", 99:"UNKNOWN"})
df["SPEAKS_NATIVE_LANGUAGE"] = df["SPEAKS_NATIVE_LANGUAGE"].map({1:"YES", 2:"NO",97:"DOES NOT APPLY",98:"IGNORED", 99:"UNKNOWN"})
df["DIABETES"] = df["DIABETES"].map({1:'YES', 2:'NO', 97:'DOES NOT APPLY', 98:'IGNORED', 99:'UNKNOWN'})
df["COPD"] = df["COPD"].map({1:'YES', 2:'NO', 97:'DOES NOT APPLY', 98:'IGNORED', 99:'UNKNOWN'})
df["ASTHMA"] = df["ASTHMA"].map({1:'YES', 2:'NO', 97:'DOES NOT APPLY', 98:'IGNORED', 99:'UNKNOWN'})
df["INMUSUPR"] = df["INMUSUPR"].map({1:'YES', 2:'NO', 97:'DOES NOT APPLY', 98:'IGNORED', 99:'UNKNOWN'})
df["HYPERTENSION"] = df["HYPERTENSION"].map({1:'YES', 2:'NO', 97:'DOES NOT APPLY', 98:'IGNORED', 99:'UNKNOWN'})
df["OTHER_DISEASE"] = df["OTHER_DISEASE"].map({1:"YES", 2:"NO",97:"DOES NOT APPLY",98:"IGNORED",99:"UNKNOWN"})
df["CARDIOVASCULAR"] = df["CARDIOVASCULAR"].map({1:"YES", 2:"NO",97:"DOES NOT APPLY",98:"IGNORED",99:"UNKNOWN"})
df["OBESITY"] = df["OBESITY"].map({1:"YES", 2:"NO",97:"DOES NOT APPLY",98:"IGNORED",99:"UNKNOWN"})
df["CHRONIC_KIDNEY"] = df["CHRONIC_KIDNEY"].map({1:"YES", 2:"NO",97:"DOES NOT APPLY",98:"IGNORED",99:"UNKNOWN"})
df["TOBACCO"] = df["TOBACCO"].map({1:"YES", 2:"NO",97:"DOES NOT APPLY",98:"IGNORED",99:"UNKNOWN"})
df["ANOTHER CASE"] = df["ANOTHER CASE"].map({1:"YES", 2:"NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99:"UNKNOWN"})
df["MIGRANT"] = df["MIGRANT"].map({1:"YES", 2:"NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99:"UNKNOWN"})
df["ICU"] = df["ICU"].map({1:"YES", 2:"NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99:"UNKNOWN"})
df["OUTCOME"] = df["OUTCOME"].map({1:"POSITIVE", 2:"NEGATIVE", 3:"PENDING"})
df["NATIONALITY"] = df["NATIONALITY"].map({1:"MEXICAN", 2:"FOREIGN", 99:"UNKNOWN"})

translator = Translator()

# Function to translate to English and convert to PropCase
def translate_and_format(country):
    # Check if the country value is '99' and return it unchanged
    if country == '99':
        return country

    try:
        # Translate the country name to English
        translated = translator.translate(country, src='es', dest='en').text
        return translated.title()  # Convert to PropCase
    except Exception as e:
        print(f"Error translating '{country}': {e}")
        return country  # Return original if there's an error

# Apply the function to the DataFrame
df['COUNTRY OF ORIGIN'] = df['COUNTRY OF ORIGIN'].apply(translate_and_format)

# Change the value of 99 in country of origin to Mexico if the value of nationality is Mexican
df.loc[df['NATIONALITY'] == 'MEXICAN', 'COUNTRY OF ORIGIN'] = 'Mexico'

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
st.header('Patient Summary by Country of Origin')
st.dataframe(country_summary_filtered)
