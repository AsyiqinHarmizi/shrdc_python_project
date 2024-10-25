import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go

# Load dataset with error handling
try:
    df = pd.read_csv('dataset.csv')
except FileNotFoundError:
    st.error("The dataset file 'dataset.csv' was not found.")
    st.stop()  # Stop execution if file is not found

def run_visualization():
    st.title("Visualizations")
    bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    labels = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100']
    
    # Ensure 'AGE' column exists and create binned age categories
    if 'AGE' in df.columns:
        df['age_binned'] = pd.cut(df['AGE'], bins=bins, labels=labels, right=False)
    else:
        st.error("The dataset does not contain an 'AGE' column.")
        st.stop()

    # Create tabs for different visualizations
    tab1, tab2, tab3 = st.tabs(["Age Distribution", "Histogram of Age", "Disease Correlations"])

    # Age Distribution Tab
    with tab1:
        st.subheader("Distribution of Individuals Across Age Groups")
        
        # Filter options for age groups
        selected_age_groups = st.multiselect(
            "Select Age Groups to Display:",
            options=list(df['age_binned'].unique()),  # Convert to list for compatibility
            default=list(df['age_binned'].unique())
        )

        # Filter the DataFrame based on user selection
        if selected_age_groups:
            filtered_df = df[df['age_binned'].isin(selected_age_groups)]
        else:
            filtered_df = df

        # Count occurrences for age groups
        age_binned_counts = filtered_df['age_binned'].value_counts().sort_index()

        # Create the bar chart
        fig_age_distribution = px.bar(
            x=age_binned_counts.index,
            y=age_binned_counts.values,
            labels={'x': 'Age Group', 'y': 'Number of Individuals'},
            title='Distribution of Individuals Across Age Groups'
        )
        fig_age_distribution.update_layout(xaxis_tickangle=-45)

        # Display chart
        st.plotly_chart(fig_age_distribution)

    # Intubation Rates Tab
    with tab2:
        # Add slider to adjust bin size
        bin_size = st.slider("Select Bin Size for Histogram", min_value=5, max_value=20, value=10, step=1)

        # Create histogram
        fig_age_histogram = go.Figure(data=[go.Histogram(
            x=df['AGE'],
            xbins=dict(start=min(bins), end=max(bins), size=bin_size),
            marker=dict(color='blue', line=dict(color='black', width=1)),
            name='Age Distribution'
        )])

        # Update layout
        fig_age_histogram.update_layout(
            title="Histogram of Age",
            xaxis_title="Age",
            yaxis_title="Frequency",
            xaxis=dict(tickvals=bins),
            bargap=0,
            width=800,
            height=600
        )

        # Display histogram
        st.plotly_chart(fig_age_histogram)

    # Disease Correlations Tab
    with tab3:
        st.subheader("Correlations Between Diseases and ICU Admission")
        disease_columns = ['DIABETES', 'COPD', 'ASTHMA', 'INMUSUPR', 
                           'HYPERTENSION', 'CARDIOVASCULAR', 
                           'OBESITY', 'CHRONIC_KIDNEY', 'TOBACCO', 'ICU']

        # Map diseases to binary values, handling cases with different or missing values
        for column in disease_columns:
            if column in df.columns:
                df[column] = df[column].map({'YES': 1, 'NO': 0}).fillna(0)
            else:
                st.warning(f"The column '{column}' is not present in the dataset.")
        
        # Preview the processed disease columns
        st.write(df[disease_columns].head())

        # Calculate and display the correlation matrix
        correlation_matrix = df[disease_columns].corr(method='pearson')
        st.write(correlation_matrix)

# Run the visualization function
run_visualization()
