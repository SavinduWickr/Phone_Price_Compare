import os
import pandas as pd
from bs4 import BeautifulSoup

def scrape_and_save_to_excel(html_filename, excel_filename):
    products = []
    prices = []

    with open(html_filename, "r", encoding="utf-8") as file:
        html = file.read()

    soup = BeautifulSoup(html, "html.parser")
    in_stock_tags = soup.find_all("h4", text="In Stock")

    for in_stock_tag in in_stock_tags:
        caption_div = in_stock_tag.find_parent("div", class_="caption")

        if caption_div:
            product_name = caption_div.find("a").text.strip()
            price = caption_div.find("p", class_="price").text.strip()
            products.append(product_name)
            prices.append(price)

    data = {"Product Name": products, "Price": prices}
    df = pd.DataFrame(data)

    # Save data to a separate sheet in the Excel file
    with pd.ExcelWriter(excel_filename, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
        sheet_name = os.path.splitext(os.path.basename(html_filename))[0]  # Use the HTML file name as the sheet name
        df.to_excel(writer, sheet_name=sheet_name, index=False)

def main():
    # Specify the directory path where your HTML files are located
    directory_path = "C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\html\\Emobile\\"

    # List all files in the directory
    all_files = os.listdir(directory_path)

    # Filter HTML files by checking the file extension
    html_files = [os.path.join(directory_path, file) for file in all_files if file.endswith(".html")]

    # Name of the Excel file to save the data
    excel_file = "C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\data_src\\instock_data\\Emobile_data_combined.xlsx"

    # Create the Excel file with a single dummy sheet
    with pd.ExcelWriter(excel_file, engine="openpyxl", mode="w") as writer:
        df = pd.DataFrame({"Placeholder": [0]})
        df.to_excel(writer, sheet_name="Placeholder", index=False)

    # Iterate through the HTML files and save data to separate sheets
    for html_file in html_files:
        scrape_and_save_to_excel(html_file, excel_file)

    # Read all sheets from the Excel file and combine them into one DataFrame
    combined_df = pd.concat(pd.read_excel(excel_file, sheet_name=None), ignore_index=True)

    # Drop the "Placeholder" column
    combined_df = combined_df.drop(columns=["Placeholder"])

    # Remove empty rows
    combined_df = combined_df.dropna()

    # Save the combined data to a new Excel file
    combined_excel_file = "C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\data_src\\instock_data\\Emobile.xlsx"
    combined_df.to_excel(combined_excel_file, index=False)

    # Remove the original Excel file
    os.remove(excel_file)

    print("Data has been combined, 'Placeholder' column removed, empty rows removed, and the original Excel file has been deleted.")

if __name__ == "__main__":
    main()
