from bs4 import BeautifulSoup
import pandas as pd

# Parse the HTML content from an HTML file (replace 'sample.html' with your file path)
with open('C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\html\\Celltronics\\page_1.html', 'r',
          encoding='utf-8') as file:
    html = file.read()

# Parse the HTML content
soup = BeautifulSoup(html, 'html.parser')

# Initialize lists to store the extracted data
product_names = []
product_links = []
prices = []

# Find all <div> elements with class containing "instock"
product_divs = soup.find_all('div', class_=lambda x: x and 'instock' in x)

# Iterate through the product divs
for div in product_divs:
    # Extract the product name and link from the <h3> tag
    h3_tag = div.find('h3', class_='wd-entities-title')
    if h3_tag:
        product_name = h3_tag.text.strip()
        product_link = h3_tag.find('a')['href']

        # Extract the price from the <span> tag
        price_element = div.find('span', class_='woocommerce-Price-amount amount')

        # Check if a price is found
        if price_element:
            price = price_element.text.strip()
            product_names.append(product_name)
            product_links.append(product_link)
            prices.append(price)

# Check if any data was extracted
if product_names:
    # Create a pandas DataFrame to store the data
    data = {
        'Product Name': product_names,
        'Product Link': product_links,
        'Price': prices
    }
    df = pd.DataFrame(data)

    # Save the DataFrame to an Excel file (replace 'output.xlsx' with your desired file name)
    df.to_excel('C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\data_src\\instock_data\\Celltronic.xlsx',
                index=False)

    print("Data has been saved")
else:
    print("No products with prices found in the HTML.")
