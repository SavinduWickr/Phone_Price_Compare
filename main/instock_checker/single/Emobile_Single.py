import pandas as pd
from bs4 import BeautifulSoup

# Load the HTML file
with open("Emobile.html", "r", encoding="utf-8") as file:
    html = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Initialize empty lists to store the data
products = []
prices = []

# Find all the <h4> tags with "In Stock" text
in_stock_tags = soup.find_all("h4", text="In Stock")

# Loop through the in-stock tags and extract data
for in_stock_tag in in_stock_tags:
    # Find the parent <div> with class "caption"
    caption_div = in_stock_tag.find_parent("div", class_="caption")

    if caption_div:
        # Find the product name within the <a> tag
        product_name = caption_div.find("a").text.strip()

        # Find the price within the <p> tag with class "price"
        price = caption_div.find("p", class_="price").text.strip()

        # Append the data to the respective lists
        products.append(product_name)
        prices.append(price)

# Create a DataFrame to store the data
data = {"Product Name": products, "Price": prices}
df = pd.DataFrame(data)

# Save the data to an Excel file
df.to_excel("Emobile_data.xlsx", index=False)

print("Data has been scraped and saved to Emobile_data.xlsx")
