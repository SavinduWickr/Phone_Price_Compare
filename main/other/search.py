import pandas as pd

# Load the Excel file
df = pd.read_excel("C:\\Users\\wickr\\Desktop\\Phone_price_compare\\data_src\\Combined_data.xlsx")

# Input maximum price, minimum RAM, and minimum storage from the user
max_price = float(input("Enter maximum price: "))
min_ram = input("Enter minimum RAM (e.g., 4): ")  # Input RAM without 'GB'
min_storage = input("Enter minimum storage (e.g., 64): ")  # Input storage without 'GB' or 'TB'

# Convert RAM and storage columns to integers
df['RAM'] = df['RAM'].str.extract('(\d+)').astype(float).fillna(0).astype(int)
df['Storage'] = df['Storage'].str.extract('(\d+)').astype(float).fillna(0).astype(int)

# Define a function to filter the data
def filter_products(max_price, min_ram, min_storage):
    try:
        min_ram = int(min_ram)
    except ValueError:
        min_ram = 0
    try:
        min_storage = int(min_storage)
    except ValueError:
        min_storage = 0

    filtered_df = df[
        (df['Price'] <= max_price) &
        (df['RAM'] >= min_ram) &
        (df['Storage'] >= min_storage)
    ]
    return filtered_df

# Filter the data based on user input
filtered_products = filter_products(max_price, min_ram, min_storage)

# Display the filtered product names
if not filtered_products.empty:
    print("Products matching your criteria:")
    for product_name in filtered_products['Product Name']:
        print(product_name)
else:
    print("No products match your criteria.")

# Optionally, you can save the filtered data to a new Excel file
filtered_products.to_excel("C:\\Users\\wickr\\Desktop\\Phone_price_compare\\data_src\\Filtered_data.xlsx", index=False)
