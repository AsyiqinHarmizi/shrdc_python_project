
import pandas as pd
from googletrans import Translator

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

df.to_csv("cleaned_dataset.csv", index=False)