import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

st.subheader('DATA VISUALIZATION')
st.subheader('Descriptive Statistics')
st.caption('After data cleaning and data validation was done')


# Load the dataset
df = pd.read_csv('dataset.csv')

# Map categorical variables to meaningful labels
df["SEX"] = df["SEX"].map({1: "FEMALE", 2: "MALE", 99: "UNKNOWN"})
df["HOSPITALIZED"] = df["HOSPITALIZED"].map({1: "NO", 2: "YES", 99: "UNKNOWN"})
df["INTUBATED"] = df["INTUBATED"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["PNEUMONIA"] = df["PNEUMONIA"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["PREGNANCY"] = df["PREGNANCY"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["OTHER_DISEASE"] = df["OTHER_DISEASE"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["CARDIOVASCULAR"] = df["CARDIOVASCULAR"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["OBESITY"] = df["OBESITY"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["CHRONIC_KIDNEY"] = df["CHRONIC_KIDNEY"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["TOBACCO"] = df["TOBACCO"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["SPEAKS_NATIVE_LANGUAGE"] = df["SPEAKS_NATIVE_LANGUAGE"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["DIABETES"] = df["DIABETES"].map({1: 'YES', 2: 'NO', 97: 'DOES NOT APPLY', 98: 'IGNORED', 99: 'UNKNOWN'})
df["COPD"] = df["COPD"].map({1: 'YES', 2: 'NO', 97: 'DOES NOT APPLY', 98: 'IGNORED', 99: 'UNKNOWN'})
df["ASTHMA"] = df["ASTHMA"].map({1: 'YES', 2: 'NO', 97: 'DOES NOT APPLY', 98: 'IGNORED', 99: 'UNKNOWN'})
df["INMUSUPR"] = df["INMUSUPR"].map({1: 'YES', 2: 'NO', 97: 'DOES NOT APPLY', 98: 'IGNORED', 99: 'UNKNOWN'})
df["HYPERTENSION"] = df["HYPERTENSION"].map({1: 'YES', 2: 'NO', 97: 'DOES NOT APPLY', 98: 'IGNORED', 99: 'UNKNOWN'})
df["ANOTHER CASE"] = df["ANOTHER CASE"].map({1: 'YES', 2: 'NO', 97: 'DOES NOT APPLY', 98: 'IGNORED', 99: 'UNKNOWN'})
df["MIGRANT"] = df["MIGRANT"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["ICU"] = df["ICU"].map({1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"})
df["OUTCOME"] = df["OUTCOME"].map({1: "POSITIVE", 2: "NEGATIVE", 3: "PENDING"})
df["NATIONALITY"] = df["NATIONALITY"].map({1: "MEXICAN", 2: "FOREIGN", 99: "UNKNOWN"})

# Create age bins and labels
age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
age_labels = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100']

# Create the AGE_GROUP variable
df['AGE_GROUP'] = pd.cut(x=df['AGE'], bins=age_bins, labels=age_labels, right=False)

# Create DECEASED variable based on date_of_death
df['DECEASED'] = df['DATE_OF_DEATH'].notna()  # True if date_of_death is not null

# Replace "IGNORED" values with NaN in the TOBACCO and DIABETES columns
df['DIABETES'].replace("IGNORED", pd.NA, inplace=True)
df['COPD'].replace("IGNORED", pd.NA, inplace=True)
df['ASTHMA'].replace("IGNORED", pd.NA, inplace=True)
df['INMUSUPR'].replace("IGNORED", pd.NA, inplace=True)
df['HYPERTENSION'].replace("IGNORED", pd.NA, inplace=True)
df['CARDIOVASCULAR'].replace("IGNORED", pd.NA, inplace=True)
df['OBESITY'].replace("IGNORED", pd.NA, inplace=True)
df['CHRONIC_KIDNEY'].replace("IGNORED", pd.NA, inplace=True)
df['TOBACCO'].replace("IGNORED", pd.NA, inplace=True)

# Drop rows with NaN values in TOBACCO and DIABETES
df.dropna(subset=['DIABETES', 'COPD', 'ASTHMA', 'INMUSUPR', 'HYPERTENSION','CARDIOVASCULAR', 'OBESITY', 'CHRONIC_KIDNEY', 'TOBACCO'], inplace=True)
col1, col2 = st.columns(2)

with col1:
    # Create a mapping for deceased status
    deceased_map = {True: 'Deceased', False: 'Not Deceased'}
    df['DECEASED_STATUS'] = df['DECEASED'].map(deceased_map)

    # Create a multi-select widget for deceased status
    deceased_options = st.multiselect(
        'Select deceased status to filter (At least 1 required):',
        options=['Deceased', 'Not Deceased'],  # Multi-select options
        default=['Deceased', 'Not Deceased']   # Default selection is all options
    )

    # Check if no options are selected
    if not deceased_options:
        st.warning("Please select at least one deceased status.")
        st.stop()  # Stop execution until the user selects at least one option

with col2:
    # Multi-select for choosing sex
    selected_SEX = st.multiselect(
        "Select Sex (At least 1 required)", 
        df['SEX'].unique(), 
        default=df['SEX'].unique()
    )

    # Check if no sex options are selected
    if not selected_SEX:
        st.warning("Please select at least one sex.")
        st.stop()  # Stop execution until the user selects at least one option

# Filter the DataFrame based on selected deceased status and sex
filtered_df = df[
    (df['DECEASED_STATUS'].isin(deceased_options)) &
    (df['SEX'].isin(selected_SEX))
]

col1, col2 = st.columns(2)

with col1:
    st.caption("Pie Chart on Diabetes")

    # Count the occurrences of diabetes in the filtered data
    diabetes_counts = filtered_df['DIABETES'].value_counts().reset_index()
    diabetes_counts.columns = ['Diabetes', 'Count']

    # Create a pie chart using Plotly
    fig = px.pie(diabetes_counts, names='Diabetes', values='Count', title="Diabetes")

    # Display the pie chart in Streamlit
    st.plotly_chart(fig)

with col2:
    st.caption("Bar Chart on Tobacco Use")

    # Count the occurrences of tobacco use in the filtered data
    tobacco_counts = filtered_df['TOBACCO'].value_counts().reset_index()
    tobacco_counts.columns = ['Tobacco Use', 'Count']

    # Create a bar chart using Plotly
    fig = px.bar(tobacco_counts, x='Tobacco Use', y='Count', title="Tobacco Use")

    # Display the bar chart in Streamlit
    st.plotly_chart(fig)

col1, col2 = st.columns(2)

with col1:
    st.caption("Donut Chart on COPD Status")

    # Filter out rows with 'IGNORED' and 'DOES NOT APPLY' for COPD
    filtered_df_copd = filtered_df[~filtered_df["COPD"].isin(["IGNORED", "DOES NOT APPLY"])]

    # Count the occurrences of COPD status in the filtered data
    copd_counts = filtered_df_copd["COPD"].value_counts().reset_index()
    copd_counts.columns = ["COPD Status", "Count"]

    # Create a donut chart using Plotly
    fig = px.pie(
        copd_counts, 
        names="COPD Status", 
        values="Count", 
        title="COPD Status", 
        hole=0.4  # This makes it a donut chart
    )

    # Display the chart in Streamlit
    st.plotly_chart(fig)

with col2:
    st.caption("Pie Chart on ASTHMA")

    # Count the occurrences of asthma in the filtered data
    asthma_counts = filtered_df['ASTHMA'].value_counts().reset_index()
    asthma_counts.columns = ['Asthma Status', 'Count']

    # Create a pie chart using Plotly
    fig_asthma = px.pie(asthma_counts, names='Asthma Status', values='Count', title="ASTHMA Status")

    # Display the pie chart in Streamlit
    st.plotly_chart(fig_asthma)



st.subheader('Inferential Statistics')
st.markdown("Correlation Analysis")
tab1, tab2 = st.tabs(["Heatmap", "Table"])
with tab1:
    st.markdown("Correlation Matrix Heatmap")
    # Assuming df is already created and mapped as per your previous code
    # Convert disease columns to binary values
    disease_columns = ['DIABETES', 'COPD', 'ASTHMA', 'INMUSUPR', 'HYPERTENSION', 
                   'CARDIOVASCULAR', 'OBESITY', 'CHRONIC_KIDNEY', 'TOBACCO', 'ICU']

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

    # Calculate correlation matrix
    correlation_matrix = df[disease_columns].corr(method='pearson')

    import plotly.graph_objects as go  # Import plotly.graph_objects for go.Heatmap

    # Display the correlation matrix using Plotly heatmap
    fig = go.Figure(data=go.Heatmap(
        z=correlation_matrix.values,
        y=correlation_matrix.columns,
        x=correlation_matrix.index,
        colorscale='RdBu',
        zmin=-1, zmax=1,
        hoverongaps=False,
        colorbar=dict(title="Correlation", titleside="right")
    ))

    fig.update_layout(
        title='Correlation Heatmap of Diseases and ICU Admission',
        xaxis_nticks=36,
        autosize=False,
        width=800,
        height=600,
        title_x=0.5
    )     

    # Display the heatmap in Streamlit
    st.plotly_chart(fig)
with tab2:
    # Optionally, display the correlation matrix as a table
    st.markdown("Correlation Matrix Table")
    st.dataframe(correlation_matrix)


st.markdown("Variable : Age")
tab1, tab2 = st.tabs(["Bar Chart", "Histogram"])
with tab1:
    # Create a bar plot using Seaborn
    fig, ax = plt.subplots()  # Create a Matplotlib figure and axis
    sns.countplot(x='AGE_GROUP', data=df, ax=ax)

    # Add labels and title
    ax.set_xlabel('Age Group')
    ax.set_ylabel('Frequency')
    ax.set_title('Age Group Distribution')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)  # Rotate x-axis labels for readability

    # Display the bar chart in Streamlit
    st.pyplot(fig)

with tab2:
    age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # Plot histogram using Matplotlib
    fig, ax = plt.subplots()  # Create a Matplotlib figure and axis
    ax.hist(df['AGE'], bins=age_bins, edgecolor='black')

    # Add labels and title
    ax.set_xlabel('Age')
    ax.set_ylabel('Frequency')
    ax.set_title('Age Distribution')
    ax.set_xticks(age_bins)  # Set x-axis ticks to match age bin boundaries

    # Display the plot in Streamlit
    st.pyplot(fig)

st.markdown("Distribution of cases by gender & age group")
# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create a grouped bar plot using Seaborn
sns.countplot(x='AGE_GROUP', hue='SEX', data=df, ax=ax)

# Add labels and title
ax.set_xlabel('Age Group')
ax.set_ylabel('Count')
ax.set_title('Distribution of Cases by Gender & Age Group')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
ax.legend(title='Gender')

# Add data labels on top of each bar
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='bottom', fontsize=10, color='black', 
                xytext=(0, 5),  # Offset text by 5 points
                textcoords='offset points')

# Display the plot in Streamlit
st.pyplot(fig)

st.markdown("Variable: Intubated")
# Counting the number of patients who required intubation
intubation_count = df['INTUBATED'].value_counts()
intubation_yes_count = intubation_count.get("YES", 0)

# Display the count in Streamlit
st.write(f"Number of patients who required intubation: {intubation_yes_count}")

# Create a figure and axis
fig, ax = plt.subplots()

# Plotting the bar graph using Seaborn
sns.barplot(x=intubation_count.index, y=intubation_count.values, ax=ax)

# Add labels and title
ax.set_xlabel('Intubation')
ax.set_ylabel('Number of Patients')
ax.set_title('Intubation Status Bar Chart')

# Adding value labels to each column
ax.bar_label(ax.containers[0], fmt='%.0f')

# Display the plot in Streamlit
st.pyplot(fig)


st.markdown("Bar Chart of Deceased Patients by Disease")
# Assuming df is already created and contains the necessary mappings
df_deceased = df[df['DATE_OF_DEATH'].notnull()]

# List of disease columns
disease_columns = ['DIABETES', 'COPD', 'ASTHMA', 'INMUSUPR', 'HYPERTENSION', 
                   'CARDIOVASCULAR', 'OBESITY', 'CHRONIC_KIDNEY', 'TOBACCO']

# Get the number of rows containing "YES" (1) for each disease column and map to disease names
yes_counts_dict = {col: df_deceased[col].value_counts().get(1, 0) for col in disease_columns}

# Convert the dictionary to a DataFrame
yes_counts_df = pd.DataFrame(list(yes_counts_dict.items()), columns=['Disease', 'Yes_Count'])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 6))

# Create a bar plot using seaborn
bar_plot = sns.barplot(data=yes_counts_df, x='Disease', y='Yes_Count', ax=ax)

# Add labels and title
ax.set_xlabel('Disease')
ax.set_ylabel('Number of Deceased Patients')
ax.set_title('Number of Deceased Patients for Each Disease')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')  # Rotate x-axis labels for better readability

# Add data labels on top of each bar
for p in bar_plot.patches:
    bar_plot.annotate(f'{int(p.get_height())}', 
                      (p.get_x() + p.get_width() / 2., p.get_height()), 
                      ha='center', va='bottom', fontsize=10, color='black', 
                      xytext=(0, 5),  # Offset text by 5 points
                      textcoords='offset points')

# Display the plot in Streamlit
st.pyplot(fig)