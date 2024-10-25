import streamlit as st
import pandas as pd

def run_data_analysis():
    st.title("Data Analysis")

    # Load the dataset
    df = pd.read_csv('dataset.csv')
    st.dataframe(df)

    # Mapping Columns
    with st.spinner("Mapping columns..."):
        mapping_dict = {
            "SEX": {1: "FEMALE", 2: "MALE", 99: "UNKNOWN"},
            "HOSPITALIZED": {1: "NO", 2: "YES", 99: "UNKNOWN"},
            "INTUBATED": {1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"},
            "PNEUMONIA": {1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"},
            "PREGNANCY": {1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"},
            "SPEAKS_NATIVE_LANGUAGE": {1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"},
            "DIABETES": {1: 'YES', 2: 'NO', 97: 'DOES NOT APPLY', 98: 'IGNORED', 99: 'UNKNOWN'},
            "COPD": {1: 'YES', 2: 'NO', 97: 'DOES NOT APPLY', 98: 'IGNORED', 99: 'UNKNOWN'},
            "ASTHMA": {1: 'YES', 2: 'NO', 97: 'DOES NOT APPLY', 98: 'IGNORED', 99: 'UNKNOWN'},
            "INMUSUPR": {1: 'YES', 2: 'NO', 97: 'DOES NOT APPLY', 98: 'IGNORED', 99: 'UNKNOWN'},
            "HYPERTENSION": {1: 'YES', 2: 'NO', 97: 'DOES NOT APPLY', 98: 'IGNORED', 99: 'UNKNOWN'},
            "OTHER_DISEASE": {1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"},
            "CARDIOVASCULAR": {1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"},
            "OBESITY": {1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"},
            "CHRONIC_KIDNEY": {1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"},
            "TOBACCO": {1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"},
            "ANOTHER CASE": {1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"},
            "MIGRANT": {1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"},
            "ICU": {1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"},
            "OUTCOME": {1: "POSITIVE", 2: "NEGATIVE", 3: "PENDING"},
            "NATIONALITY": {1: "MEXICAN", 2: "FOREIGN", 99: "UNKNOWN"}
            }
            # Map the values in the DataFrame
        for column, mapping in mapping_dict.items():
            df[column] = df[column].map(mapping)

    st.write("Updated DataFrame:")
    st.dataframe(df)

    # Binning 'AGE' column
    bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    labels = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100']

    df['age_binned'] = pd.cut(df['AGE'], bins=bins, labels=labels, right=False)

    st.write("DataFrame with Binned Age Groups:")
    st.dataframe(df)

run_data_analysis()
