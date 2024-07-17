import os
import pandas as pd
from bs4 import BeautifulSoup

# List of product names and their corresponding directories
product_info = [
    {"name": "X_mobile", "directory": "C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\html\\X_mobile"},
    {"name": "Dealz_Woot", "directory": "C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\html\\Dealz_Woot"},
    {"name": "Present_solution", "directory": "C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\html\\Present_solution"},
    {"name": "Doctor_Mobile", "directory": "C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\html\\Doctor_Mobile"}
]

# Iterate through each product
for product_data in product_info:
    name = product_data["name"]
    html_directory = product_data["directory"]

    # Initialize empty lists to store product names and prices for the current product
    product_names = []
    prices = []

    # Iterate through all HTML files in the directory
    for filename in os.listdir(html_directory):
        if filename.endswith(".html"):
            # Create the full path to the HTML file
            file_path = os.path.join(html_directory, filename)

            # Load the HTML file
            with open(file_path, "r", encoding="utf-8") as file:
                html_content = file.read()

            # Parse the HTML using BeautifulSoup
            soup = BeautifulSoup(html_content, "html.parser")

            # Find all product boxes
            product_boxes = soup.find_all("div", class_="span2 product_box")

            # Iterate through each product box
            for product_box in product_boxes:
                # Find the product name
                product_name = product_box.find("h5").find("a").text.strip()

                # Find the price
                price = product_box.find("span", class_="bestprice").text.strip()

                # Append the data to the respective lists
                product_names.append(product_name)
                prices.append(price)

    # Create a DataFrame to store the data for the current product
    data = {"Product Name": product_names, "Price": prices}
    df = pd.DataFrame(data)

    # Save the data to an Excel file for the current product
    output_file = f"C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\data_src\\instock_data\\{name}.xlsx"
    df.to_excel(output_file, index=False)

    print(f"Data for {name} saved to {output_file}")
