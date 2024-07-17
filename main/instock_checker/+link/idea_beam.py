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

    # Initialize empty lists to store product names, prices, and links for the current product
    product_names = []
    prices = []
    product_links = []  # Add a list to store product links

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
                product_name_tag = product_box.find("h5").find("a")
                if product_name_tag:
                    product_name = product_name_tag.text.strip()

                    # Find the product link
                    product_link = product_name_tag['href']

                    # Find the price
                    price_tag = product_box.find("span", class_="bestprice")
                    price = price_tag.text.strip() if price_tag else 'Price not found'

                    # Append the data to the respective lists
                    product_names.append(product_name)
                    product_links.append(product_link)  # Append the product link
                    prices.append(price)

    # Create a DataFrame to store the data for the current product
    data = {"Product Name": product_names, "Product Link": product_links, "Price": prices}
    df = pd.DataFrame(data)

    # Save the data to an Excel file for the current product
    output_file = f"C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\data_src\\instock_data\\{name}.xlsx"
    df.to_excel(output_file, index=False)

    print(f"Data for {name} saved to {output_file}")
