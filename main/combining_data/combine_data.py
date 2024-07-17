import pandas as pd

# Load the Updated_data.xlsx and Updated_data_Life.xlsx files
df_updated = pd.read_excel("C:\\Users\\wickr\\Desktop\\Phone_price_compare\\data_src\\Emobile_data_sorted.xlsx")
df_updated_life = pd.read_excel("C:\\Users\\wickr\\Desktop\\Phone_price_compare\\data_src\\Updated_data_Life.xlsx")

# Define a custom function to handle TB and GB values
def convert_to_gb(value):
    if 'TB' in str(value):
        value = float(value.replace('TB', '').strip()) * 1024  # Convert TB to GB
    elif 'GB' in str(value):
        value = float(value.replace('GB', '').strip())  # Remove GB
    return value

# Apply the custom function to the "RAM" and "Storage" columns
df_updated["RAM"] = df_updated["RAM"].apply(convert_to_gb)
df_updated_life["RAM"] = df_updated_life["RAM"].apply(convert_to_gb)

df_updated["Storage"] = df_updated["Storage"].apply(convert_to_gb)
df_updated_life["Storage"] = df_updated_life["Storage"].apply(convert_to_gb)

# Add a new column with the specified names
df_updated.insert(0, 'shop', 'Emobile')
df_updated_life.insert(0, 'shop', 'Life Mobile')

# Concatenate the two dataframes
combined_df = pd.concat([df_updated, df_updated_life], ignore_index=True)

# Save the combined dataframe to a new Excel file
combined_df.to_excel("C:\\Users\\wickr\\Desktop\\Phone_price_compare\\data_src\\Combined_data.xlsx", index=False)

print("Combined data has been saved to Combined_data.xlsx")
