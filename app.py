import pandas as pd
import streamlit as st

# Load your cleaned data
try:
    cleaned_data = pd.read_csv('Cleaned_Ankle_Fixation_Data.csv')
    st.write("Data loaded successfully!")
except Exception as e:
    st.write("Error loading data:", e)

# Function to calculate the Lindy score
def calculate_lindy_score(row):
    age_score = row['age'] / 100
    citation_score = row['total_citations'] / (row['citations_per_year'] + 1)
    return age_score + citation_score

# Apply the Lindy score calculation to each row
cleaned_data['Lindy_Score'] = cleaned_data.apply(calculate_lindy_score, axis=1)

# Create a new DataFrame with the required columns
lindy_data = cleaned_data[['technique', 'age', 'total_citations', 'citations_per_year', 'Lindy_Score']]

# Set the title of the app
st.title("Ankle Fixation Technique Lindy Score Calculator")

# Display the DataFrame
st.write("Here is the cleaned data with Lindy Scores:")
st.dataframe(lindy_data)

# Optional: Display a summary of the Lindy scores
st.write("Lindy Scores Summary:")
st.bar_chart(lindy_data.set_index('technique')['Lindy_Score'])
