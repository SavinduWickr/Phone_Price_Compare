import pandas as pd
import re
import numpy as np  # Import numpy to handle NaN values

filename = "Genuis_Mobile.xlsx"
# Load the Excel file
df = pd.read_excel(f"C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\data_src\\instock_data\\{filename}")

# Initialize lists to store RAM and storage information
ram = []
storage = []

# Define a function to extract RAM and storage information
def extract_ram_and_storage(product_name):
    gb_matches = re.findall(r'(\d+)GB', product_name)
    tb_matches = re.findall(r'(\d+)TB', product_name)

    ram_info = None
    storage_info = None

    for match in gb_matches:
        size = int(match)
        if size > 18:
            storage_info = f"{size}GB"
        else:
            ram_info = f"{size}GB"

    for match in tb_matches:
        size = int(match)
        storage_info = f"{size}TB"

    return ram_info, storage_info

# Loop through the product names twice to extract RAM and storage information
for product_name in df["Product Name"]:
    ram_info, _ = extract_ram_and_storage(product_name)
    ram.append(ram_info)

for product_name in df["Product Name"]:
    _, storage_info = extract_ram_and_storage(product_name)
    storage.append(storage_info)

# Add RAM and storage columns to the existing DataFrame
df["RAM"] = ram
df["Storage"] = storage

# Reformat the Price column by removing 'රු' and 'Rs', and commas
df["Price"] = df["Price"].str.replace('රු', '').str.replace('Rs', '').str.replace(',', '').str.split('.').str[0]

# Convert the "Price" column to float, handling empty or non-numeric values
df["Price"] = pd.to_numeric(df["Price"], errors='coerce')

# Save the updated data to a new Excel file
df.to_excel(f"C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\data_src\\ram_rom_extracted\\{filename}", index=False)

print("RAM, storage, and Price data has been extracted and saved")
