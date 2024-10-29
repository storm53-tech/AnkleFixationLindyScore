import pandas as pd

# Load your cleaned data
cleaned_data = pd.read_csv('Cleaned_Ankle_Fixation_Data.csv')

# Function to calculate the Lindy score (this is a placeholder; replace with your logic)
def calculate_lindy_score(row):
    # Example calculation (adjust with your logic)
    age_score = row['age'] / 100  # Simplified example
    citation_score = row['total_citations'] / (row['citations_per_year'] + 1)
    return age_score + citation_score  # Example logic

# Apply the Lindy score calculation to each row
cleaned_data['Lindy_Score'] = cleaned_data.apply(calculate_lindy_score, axis=1)

# Create a new DataFrame with the required columns
lindy_data = cleaned_data[['technique', 'age', 'total_citations', 'citations_per_year', 'Lindy_Score']]

# Display the final DataFrame
print(lindy_data)

