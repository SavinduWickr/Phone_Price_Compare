import requests
from bs4 import BeautifulSoup
import os

# Base URL and starting page number
base_url = "https://lifemobile.lk/product-category/mobile-phones/page/"
start_page = 1
end_page = 23  # Set the number of pages you want to scrape

# Directory to save the HTML files
save_directory = "C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\html\\Life_Mobile"

# Create the save directory if it doesn't exist
os.makedirs(save_directory, exist_ok=True)

# Headers with User-Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Iterate through pages
for page_number in range(start_page, end_page + 1):
    # Construct the URL for the current page
    url = f"{base_url}{page_number}/"

    # Send an HTTP GET request to the URL with headers
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for any HTTP errors
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve page {page_number}: {e}")
        continue

    # Parse the HTML content of the page
    try:
        soup = BeautifulSoup(response.text, 'html.parser')
    except Exception as e:
        print(f"Error parsing page {page_number}: {e}")
        continue

    # Save the HTML content to a file
    filename = os.path.join(save_directory, f"page_{page_number}.html")
    try:
        with open(filename, 'w', encoding='utf-8') as html_file:
            html_file.write(str(soup))
        print(f"Page {page_number} saved as {filename}")
    except Exception as e:
        print(f"Error saving page {page_number}: {e}")

print("Scraping completed.")
