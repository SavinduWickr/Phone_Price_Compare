import requests
from bs4 import BeautifulSoup
import os

# Base URL and starting page number
base_url = "https://celltronics.lk/product-category/mobile-phones-price-in-sri-lanka/page/"
start_page = 1
end_page = 2  # Set the number of pages you want to scrape

# Directory to save the HTML files
save_directory = "C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\html\\Celltronics"

# Create the save directory if it doesn't exist
os.makedirs(save_directory, exist_ok=True)

# Iterate through pages
for page_number in range(start_page, end_page + 1):
    # Construct the URL for the current page
    url = f"{base_url}{page_number}/?per_page=300"  # Include the per_page query parameter

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Save the HTML content to a file
        filename = os.path.join(save_directory, f"page_{page_number}.html")
        with open(filename, 'w', encoding='utf-8') as html_file:
            html_file.write(str(soup))

        print(f"Page {page_number} saved as {filename}")
    else:
        print(f"Failed to retrieve page {page_number}")

print("Scraping completed.")
