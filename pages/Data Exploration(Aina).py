import streamlit as st
st.subheader('Data Exploration')
st.caption('To understand the quality of the dataset')

import pandas as pd
df = pd.read_csv('banking.csv')

import plotly.express as px

# Multiselect for choosing multiple marital statuses
selected_statuses = st.multiselect("Select Marital Statuses", df['marital'].unique(), default=df['marital'].unique())

# Filter the data based on the selected marital statuses
filtered_df = df[df['marital'].isin(selected_statuses)]

col1, col2 = st.columns(2)
with col1:
    st.caption("Discovery on Marital Status")

    # Count the occurrences of each selected marital status
    marital_counts = filtered_df['marital'].value_counts().reset_index()
    marital_counts.columns = ['Marital Status', 'Count']

    # Create a pie chart using plotly
    fig = px.pie(marital_counts, names='Marital Status', values='Count', title="Pie Chart of Selected Marital Statuses")

    # Display the pie chart in Streamlit
    st.plotly_chart(fig)

with col2:
    st.caption("Discovery on Marital Status")
    st.bar_chart(df, x="marital", y="emp_var_rate")


import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('banking.csv')

st.header("Here are some examples of boxplot using banking data!")

col1, col2 = st.columns(2)

with col1:
    category = st.selectbox("Choose a category to group by:", df.columns.drop('marital'))
    fig, ax = plt.subplots()
    sns.boxplot(x=category,y='age', data=df, ax=ax)    
    
    st.pyplot(fig)

with col2:
    category = st.selectbox("Choose a category to group by:", df.columns.drop('loan'))
    fig, ax = plt.subplots()
    sns.boxplot(x=category, y='age', data=df, ax=ax)
    
    st.pyplot(fig)