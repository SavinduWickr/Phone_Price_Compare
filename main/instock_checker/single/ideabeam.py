import pandas as pd
from bs4 import BeautifulSoup

# Load the HTML file
with open("C:\\Users\\wickr\\Desktop\\Phone_price_compare\\html\\Doctor_Mobile\\Doctor Mobile Mobile Phone Price List in Sri Lanka 2023 22nd August.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Initialize empty lists to store product names and prices
product_names = []
prices = []

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

# Create a DataFrame to store the data
data = {"Product Name": product_names, "Price": prices}
df = pd.DataFrame(data)

# Save the data to an Excel file
output_file = "C:\\Users\\wickr\\Desktop\\Phone_price_compare\\data_src\\instock_data\\Doctor_Mobile.xlsx"
df.to_excel(output_file, index=False)

print(f"Data saved to {output_file}")
