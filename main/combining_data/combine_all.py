import pandas as pd

filename_1 = "Emobile.xlsx"
filename_2 = "Celltronic.xlsx"
filename_3 = "Genuis_Mobile.xlsx"
filename_4 = "Life_Mobile.xlsx"
filename_5 = "X_mobile.xlsx"
filename_6 = "Present_solution.xlsx"
filename_7 = "Doctor_Mobile.xlsx"
filename_8 = "Dealz_Woot.xlsx"

# File paths for the four Excel files
file_paths = [
    f"C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\data_src\\ram_rom_extracted\\{filename_1}",
    f"C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\data_src\\ram_rom_extracted\\{filename_2}",
    f"C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\data_src\\ram_rom_extracted\\{filename_3}",
    f"C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\data_src\\ram_rom_extracted\\{filename_4}",
    f"C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\data_src\\ram_rom_extracted\\{filename_5}",
    f"C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\data_src\\ram_rom_extracted\\{filename_6}",
    f"C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\data_src\\ram_rom_extracted\\{filename_7}",
    f"C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\data_src\\ram_rom_extracted\\{filename_8}",
]

# Load all four Excel files into DataFrames
dataframes = [pd.read_excel(file) for file in file_paths]

# Define a custom function to handle TB and GB values
def convert_to_gb(value):
    if 'TB' in str(value):
        value = float(value.replace('TB', '').strip()) * 1024  # Convert TB to GB
    elif 'GB' in str(value):
        value = float(value.replace('GB', '').strip())  # Remove GB
    return value

# Apply the custom function to the "RAM" and "Storage" columns for all DataFrames
for df in dataframes:
    df["RAM"] = df["RAM"].apply(convert_to_gb)
    df["Storage"] = df["Storage"].apply(convert_to_gb)

# Add a new column with the specified names for each DataFrame
for i, df in enumerate(dataframes):
    shop_name = ["Emobile", "Celltronic", "Genuis Mobile", "Life Mobile", "X Mobile", "Present Solution", "Doctor Mobile", "Dealz Woot"][i]
    df.insert(0, 'shop', shop_name)


# Concatenate all DataFrames into one
combined_df = pd.concat(dataframes, ignore_index=True)
combined_df = combined_df[combined_df['Price'] >= 20000]

# Save the combined dataframe to a new Excel file
combined_df.to_excel("C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\data_src\\multiple_combined\\Combined_data.xlsx", index=False)

print("Combined data has been saved to Combined_data.xlsx")
