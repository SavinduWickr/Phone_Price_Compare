import pandas as pd

# Load the existing combined data
combined_df = pd.read_excel("C:\\Users\\wickr\\Desktop\\Phone_price_compare\\data_src\\multiple_combined\\Combined_data.xlsx")

# Load the third file (replace 'file_path' with the path to your third file)
df_third = pd.read_excel("C:\\Users\\wickr\\Desktop\\Phone_price_compare\\data_src\\ram_rom_extracted\\Present_solution.xlsx")

# Define a custom function to handle TB and GB values
def convert_to_gb(value):
    if 'TB' in str(value):
        value = float(value.replace('TB', '').strip()) * 1024  # Convert TB to GB
    elif 'GB' in str(value):
        value = float(value.replace('GB', '').strip())  # Remove GB
    return value

# Apply the custom function to the "RAM" and "Storage" columns in the third dataframe
df_third["RAM"] = df_third["RAM"].apply(convert_to_gb)
df_third["Storage"] = df_third["Storage"].apply(convert_to_gb)

# Add a new column with the shop name for the third dataframe
df_third.insert(0, 'shop', 'Celltronic')  # Replace 'Third Shop' with the actual shop name

# Concatenate the three dataframes
combined_df = pd.concat([combined_df, df_third], ignore_index=True)

# Save the updated combined dataframe to the same Excel file
combined_df.to_excel("C:\\Users\\wickr\\Desktop\\Phone_price_compare\\data_src\\multiple_combined\\Combined_data.xlsx", index=False)

print("Combined data has been updated with the third file and saved to Combined_data.xlsx")
