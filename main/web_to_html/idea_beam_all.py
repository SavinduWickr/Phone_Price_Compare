import requests
from bs4 import BeautifulSoup
import os

# Define a list of URLs and corresponding directory names
url_directory_mapping = [
    {"url": "https://www.ideabeam.com/mobile/store/present-solution", "directory": "Present_solution"},
    {"url": "https://www.ideabeam.com/mobile/store/dealz-woot/", "directory": "Dealz_Woot"},
    {"url": "https://www.ideabeam.com/mobile/store/doctor-mobile/", "directory": "Doctor_Mobile"},
    {"url": "https://www.ideabeam.com/mobile/store/x-mobile/", "directory": "X_mobile"},
]

# Function to scrape a given URL and save HTML pages in the specified directory
def scrape_and_save(url, directory_name):
    # Create the save directory if it doesn't exist
    save_directory = os.path.join("C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\html", directory_name)
    os.makedirs(save_directory, exist_ok=True)

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the pagination links
        pagination_links = soup.find_all("li")

        # Initialize the maximum page number to 1
        max_page_number = 1

        # Iterate through the pagination links to find the maximum page number
        for link in pagination_links:
            link_text = link.find("a")
            if link_text and link_text.get("href") and "page=" in link_text.get("href"):
                page_number = int(link_text.get("href").split("=")[-1])
                max_page_number = max(max_page_number, page_number)

        print(f"Maximum page number found for {directory_name}: {max_page_number}")

        # Iterate through pages
        for page_number in range(1, max_page_number + 1):
            # Construct the URL for the current page
            page_url = f"{url}?page={page_number}"

            # Send an HTTP GET request to the page URL
            page_response = requests.get(page_url)

            if page_response.status_code == 200:
                # Parse the HTML content of the page
                page_soup = BeautifulSoup(page_response.text, 'html.parser')

                # Save the HTML content to a file
                filename = os.path.join(save_directory, f"page_{page_number}.html")
                with open(filename, 'w', encoding='utf-8') as html_file:
                    html_file.write(str(page_soup))

                print(f"Page {page_number} saved as {filename}")
            else:
                print(f"Failed to retrieve page {page_number} for {directory_name}")

        print(f"Scraping for {directory_name} completed.")
    else:
        print(f"Failed to retrieve the initial page for {directory_name}")

# Iterate through the URL-directory mappings and scrape each URL
for mapping in url_directory_mapping:
    url = mapping["url"]
    directory_name = mapping["directory"]
    scrape_and_save(url, directory_name)

print("All scraping completed.")
