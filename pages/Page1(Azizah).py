import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load dataset
df = pd.read_csv('dataset.csv')

# Map values
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

# Cut the AGE into bins
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
labels = [f'{i}-{i+10}' for i in bins[:-1]]
df['AGE_GROUP'] = pd.cut(df['AGE'], bins=bins, labels=labels, right=False)

st.header("This chart distribution show the distribution between age group")

# Plotting the bar chart using Seaborn
plt.figure(figsize=(12, 8))
sns.countplot(x='AGE_GROUP', data=df)
plt.xlabel('Age Bins')
plt.ylabel('Count')
plt.title('Distribution of Age Bins')
st.pyplot(plt)
