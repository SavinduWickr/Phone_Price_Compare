import os
import requests
from urllib.parse import urlparse, parse_qs
# List of URLs to download HTML content from
urls = [
    "https://emobile.lk/samsung-mobile-phone-price-list-sri-lanka?limit=1000",
    "https://emobile.lk/huawei-price-list-in-sri-lanka?limit=1000",
    "https://emobile.lk/xiaomi-price-list-in-sri-lanka?limit=1000",
    "https://emobile.lk/apple-iphone-price-list-in-sri-lanka?limit=1000",
    "https://emobile.lk/realme-price-list-in-sri-lanka?limit=1000",
    "https://emobile.lk/oppo-price-list-in-sri-lanka?limit=1000",
    "https://emobile.lk/poco-price-list-in-sri-lanka?limit=1000",
    "https://emobile.lk/vivo-price-list-in-sri-lanka?limit=1000",
    "https://emobile.lk/nothing-phone-price-list-in-sri-lanka?limit=1000",
    "https://emobile.lk/honor-price-list-in-sri-lanka?limit=1000",
    "https://emobile.lk/oneplus-mobile-phones-prices-in-sri-lanka?limit=1000",
    "https://emobile.lk/google-mobile-phones-prices-in-sri-lanka?limit=1000",
    "https://emobile.lk/sony-price-list-in-sri-lanka?limit=1000",
]

# Directory where you want to save the HTML files
output_directory = "C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\html\\Emobile\\"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Function to sanitize a string for use as a file name
def sanitize_filename(filename):
    return "".join([c for c in filename if c.isalnum() or c in (' ', '.', '_', '-')])

# Function to save HTML content to a file
def save_html_content(url, output_directory):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            parsed_url = urlparse(url)
            query_params = parse_qs(parsed_url.query)
            path = parsed_url.path

            # Sanitize the path and add query parameters to the file name if they exist
            sanitized_path = sanitize_filename(path)
            query_string = "_".join([f"{k}={v[0]}" for k, v in query_params.items()])
            file_name = sanitized_path + (f"_{query_string}" if query_params else "") + ".html"

            file_name = os.path.join(output_directory, file_name)

            with open(file_name, "wb") as file:
                file.write(response.content)
            print(f"Saved {url} as {file_name}")
        else:
            print(f"Failed to retrieve {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error while downloading {url}: {str(e)}")

# Loop through the URLs and save HTML content to files
for url in urls:
    save_html_content(url, output_directory)