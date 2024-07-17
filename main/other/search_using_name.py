import pandas as pd
import Levenshtein

# Load the Excel file into a DataFrame
excel_file = "C:/Users/wickr/Desktop/Phone_price_compare/data_src/multiple_combined/Combined_data.xlsx"
df = pd.read_excel(excel_file)

# Define a target phone name for comparison
target_phone_name = "14 pro max"  # Replace with the phone name you're searching for

# Define a threshold for Levenshtein similarity
similarity_threshold = 0.5  # Adjust as needed

# Create a list to store similar phone names
similar_phone_names = []

# Iterate through the DataFrame and calculate Levenshtein similarity
for index, row in df.iterrows():
    phone_name = row['Product Name']
    similarity = Levenshtein.ratio(target_phone_name.lower(), phone_name.lower())

    if similarity >= similarity_threshold:
        similar_phone_names.append(phone_name)

# Print the similar phone names
if similar_phone_names:
    print(f"Similar phone names to '{target_phone_name}':")
    for name in similar_phone_names:
        print(name)
else:
    print(f"No similar phone names found to '{target_phone_name}'.")
