import pandas as pd
import re
import os

# Define the directory containing the Excel files
directory = "C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\data_src\\instock_data"
output_directory = "C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\data_src\\ram_rom_extracted"

# List of filenames to process
filenames = ["Doctor_Mobile.xlsx", "Celltronic.xlsx", "Dealz_Woot.xlsx", "Emobile.xlsx", "Life_Mobile.xlsx", "Present_solution.xlsx", "X_mobile.xlsx"]  # Add more filenames as needed

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

# Iterate through the list of filenames
for filename in filenames:
    # Load the Excel file
    file_path = os.path.join(directory, filename)
    df = pd.read_excel(file_path)

    # Initialize lists to store RAM and storage information
    ram = []
    storage = []

    # Loop through the product names to extract RAM and storage information and convert prices
    for i, product_name in enumerate(df["Product Name"]):
        ram_info, _ = extract_ram_and_storage(product_name)
        ram.append(ram_info)

        _, storage_info = extract_ram_and_storage(product_name)
        storage.append(storage_info)

        # Convert the price string to an integer following the provided rules
        price_str = str(df.at[i, "Price"])
        price_numeric = int(re.sub(r'Rs\.|,|\..*', '', price_str))
        df.at[i, "Price"] = price_numeric  # Update the "Price" column in the DataFrame

    # Add RAM and storage columns to the existing DataFrame
    df["RAM"] = ram
    df["Storage"] = storage

    # Save the updated data to a new Excel file with error handling
    output_file_path = os.path.join(output_directory, filename)
    try:
        df.to_excel(output_file_path, index=False)
        print(f"RAM, storage, and Price data extracted and saved to {output_file_path}")
    except Exception as e:
        print("Error occurred while saving the Excel file:", str(e))
