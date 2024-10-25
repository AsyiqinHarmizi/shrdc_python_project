import pandas as pd
import plotly.express as px
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Creating multi-tab page
tab1, tab2, tab3 = st.tabs(["Demographic Data", "Intubation Data", "Timeline Chart"])

# Tab 1: Demographic Data
with tab1:
    st.header("Patient Demographics by Age, Gender, and Nationality")
    
    # Load the dataset
    df = pd.read_csv('dataset.csv')

    # Map values (as done previously)
    df["SEX"] = df["SEX"].map({1: "FEMALE", 2: "MALE", 99: "UNKNOWN"})
    df["NATIONALITY"] = df["NATIONALITY"].map({1: "MEXICAN", 2: "FOREIGN", 99: "UNKNOWN"})

    # Cut the AGE into bins
    bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    labels = [f'{i}-{i + 10}' for i in bins[:-1]]
    df['AGE_GROUP'] = pd.cut(df['AGE'], bins=bins, labels=labels, right=False)

    # Convert AGE_GROUP to a categorical type with the specified order
    df['AGE_GROUP'] = pd.Categorical(df['AGE_GROUP'], categories=labels, ordered=True)

    # User selection for nationality
    selected_nationalities = st.multiselect("Select the nationality", ['MEXICAN', 'FOREIGN'])

    # Check if the user selected any nationalities
    if selected_nationalities:
        for nationality in selected_nationalities:
            filtered_df = df[df['NATIONALITY'] == nationality]

            # Create the bar chart
            fig = px.histogram(filtered_df, x='AGE_GROUP', color='SEX', barmode='group',
                               category_orders={'AGE_GROUP': labels},
                               title=f'Distribution of Age Groups by Gender ({nationality})')

            # Display the chart
            st.plotly_chart(fig)
    else:
        st.write("Please select at least one nationality to display the charts.")

# Tab 2: Intubation Data
with tab2:
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

    st.header("Number of Deceased Patients for Each Disease")
    
    # Slider for age groups
    age_group = st.slider("Select Age Group", min_value=0, max_value=100, value=(0, 100), step=10)
    
    # Filter the data to include only deceased patients within the selected age group
    df_deceased = df[(df['DATE_OF_DEATH'].notnull()) & 
                     (df['AGE'] >= age_group[0]) & 
                     (df['AGE'] < age_group[1])]
    
    # List of disease columns
    disease_columns = ['DIABETES', 'COPD', 'ASTHMA', 'INMUSUPR', 'HYPERTENSION',
                       'CARDIOVASCULAR', 'OBESITY', 'CHRONIC_KIDNEY', 'TOBACCO']
    
    # Get the number of rows containing "YES" for each disease column and map to disease names
    yes_counts_dict = {col: df_deceased[col].value_counts().get("YES", 0) for col in disease_columns}
    yes_counts_df = pd.DataFrame(list(yes_counts_dict.items()), columns=['Disease', 'Yes_Count'])
    
    # Create a bar plot using Plotly for interactivity
    fig = px.bar(yes_counts_df, x='Disease', y='Yes_Count', 
                 labels={'Yes_Count': 'Number of Deceased Patients'},
                 title='Number of Deceased Patients for Each Disease',
                 hover_data={'Yes_Count': True})

    # Display the plot in Streamlit
    st.plotly_chart(fig)

    
    
    
    

# Tab 3: Timeline Chart
with tab3:
    st.header("Correlation between Diseases and ICU Admission")
    
    # Map disease status to binary (1 for YES, 0 for NO)
    df['DIABETES'] = df['DIABETES'].map({'YES': 1, 'NO': 0})
    df['COPD'] = df['COPD'].map({'YES': 1, 'NO': 0})
    df['ASTHMA'] = df['ASTHMA'].map({'YES': 1, 'NO': 0})
    df['INMUSUPR'] = df['INMUSUPR'].map({'YES': 1, 'NO': 0})
    df['HYPERTENSION'] = df['HYPERTENSION'].map({'YES': 1, 'NO': 0})
    df['CARDIOVASCULAR'] = df['CARDIOVASCULAR'].map({'YES': 1, 'NO': 0})
    df['OBESITY'] = df['OBESITY'].map({'YES': 1, 'NO': 0})
    df['CHRONIC_KIDNEY'] = df['CHRONIC_KIDNEY'].map({'YES': 1, 'NO': 0})
    df['TOBACCO'] = df['TOBACCO'].map({'YES': 1, 'NO': 0})
    df['ICU'] = df['ICU'].map({'YES': 1, 'NO': 0})
    
    # Calculate the correlation matrix
    disease_columns = ["DIABETES", "COPD", "ASTHMA", "INMUSUPR", "HYPERTENSION",
                       "CARDIOVASCULAR", "OBESITY", "CHRONIC_KIDNEY", "TOBACCO", "ICU"]
    correlation_matrix = df[disease_columns].corr(method='pearson')
    
    # Convert the correlation matrix to a long-form DataFrame
    correlation_df = correlation_matrix.reset_index().melt(id_vars='index')
    correlation_df.columns = ['Disease1', 'Disease2', 'Correlation']
    
    # Create an interactive heatmap using Plotly
    fig = px.imshow(correlation_matrix,
                    labels=dict(color="Correlation"),
                    x=disease_columns,
                    y=disease_columns,
                    color_continuous_scale='RdBu_r',
                    zmin=-1,
                    zmax=1,
                    title='Correlation between Diseases and ICU Admission')
    
    fig.update_layout(title_x=0.5, width=800, height=800)
    
    # Display the interactive heatmap in Streamlit
    st.plotly_chart(fig)


    
