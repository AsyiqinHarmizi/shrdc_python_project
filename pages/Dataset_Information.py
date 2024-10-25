import streamlit as st
import pandas as pd

# Example DataFrame
df = pd.read_csv("dataset.csv")

st.header('Dataset Information')
st.sidebar.write('Dataset Information')
st.write(""" 
        This dataset contains comprehensive information on COVID-19 patients in Mexico for the year 2020. It includes key variables related to patient demographics,
        clinical outcomes, and treatment details. The dataset aims to provide insights into the impact of the pandemic on various populations, highlighting trends and patterns in patient health.
         """)

st.write("\n")

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
df["COUNTRY OF ORIGIN"] = df["COUNTRY OF ORIGIN"].map({99:"UNKNOWN"})

# Convert null values in "COUNTRY OF ORIGIN" to "MEXICO" where "NATIONALITY" is "MEXICAN"
df.loc[(df["COUNTRY OF ORIGIN"].isnull()) & (df["NATIONALITY"] == "MEXICAN"), "COUNTRY OF ORIGIN"] = "Mexico"

# 1. Multiselect for columns
selected_columns = st.multiselect('Select columns to filter:', df.columns.tolist(), default=df.columns.tolist())

# Display the DataFrame with selected columns
if selected_columns:
    st.write(df[selected_columns])
else:
    st.write(df)
