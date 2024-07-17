from bs4 import BeautifulSoup
import openpyxl

# Open the HTML file
with open('C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\html\\Life_Mobile\\page_1.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Create a new Excel workbook
workbook = openpyxl.Workbook()
worksheet = workbook.active

# Define headers for the Excel sheet
worksheet.append(['Product Name', 'Product Link', 'Price'])  # Add 'Product Link' header

# Find all product items
product_items = soup.find_all('li', class_='product')

# Loop through the product items and extract data
for product_item in product_items:
    product_name = product_item.find('h2', class_='woocommerce-loop-product__title').text.strip()

    # Check if the product is instock or outofstock
    product_status = "instock" if "instock" in product_item["class"] else "outofstock"

    if product_status == "instock":
        # Find the price using the <bdi> tag
        price_container = product_item.find('bdi')
        if price_container:
            price = price_container.text.strip()
        else:
            price = 'Price not found'

        # Find the product link
        product_link = product_item.find('a', class_='woocommerce-LoopProduct-link')['href']

        # Add the data to the Excel sheet
        worksheet.append([product_name, product_link, price ])  # Add product link to the row

# Save the Excel file
workbook.save('C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\data_src\\instock_data\\Life_Mobile.xlsx')

print("Data for instock products has been scraped and saved")
