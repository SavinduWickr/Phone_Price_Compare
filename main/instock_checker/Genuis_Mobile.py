import os
import pandas as pd
from bs4 import BeautifulSoup

def scrape_and_save_to_excel(html_filename, excel_filename, processed_products):
    products = []
    prices = []
    #href_links = []

    with open(html_filename, "r", encoding="utf-8") as file:
        html = file.read()

    soup = BeautifulSoup(html, "html.parser")
    li_tags = soup.find_all("li", class_=lambda x: x and "instock" in x)

    for li_tag in li_tags:
        in_stock_tags = li_tag.find_all("h2", class_="woo-loop-product__title")
        price_tags = li_tag.find_all("span", class_="price")

        for in_stock_tag, price_tag in zip(in_stock_tags, price_tags):
            product_name = in_stock_tag.find("a").text.strip()
            price = price_tag.find("bdi").text.strip()
            #href_link = in_stock_tag.find("a")["href"].strip()

            # Check if the product is already in the set before adding it
            if product_name not in processed_products:
                processed_products.add(product_name)  # Add the product to the set
                products.append(product_name)
                prices.append(price)
                #href_links.append(href_link)

    #data = {"Product Name": products, "Link": href_links, "Price": prices}
    data = {"Product Name": products, "Price": prices}
    df = pd.DataFrame(data)

    with pd.ExcelWriter(excel_filename, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
        sheet_name = os.path.splitext(os.path.basename(html_filename))[0]
        df.to_excel(writer, sheet_name=sheet_name, index=False)

def main():
    directory_path = "C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\html\\Genuis_Mobile\\"
    all_files = os.listdir(directory_path)
    html_files = [os.path.join(directory_path, file) for file in all_files if file.endswith(".html")]
    excel_file = "C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\data_src\\instock_data\\Genuis_Mobile_data_combined.xlsx"

    with pd.ExcelWriter(excel_file, engine="openpyxl", mode="w") as writer:
        df = pd.DataFrame({"Placeholder": [0]})
        df.to_excel(writer, sheet_name="Placeholder", index=False)

    processed_products = set()  # Create a set to keep track of processed products

    for html_file in html_files:
        scrape_and_save_to_excel(html_file, excel_file, processed_products)

    combined_df = pd.concat(pd.read_excel(excel_file, sheet_name=None), ignore_index=True)
    combined_df = combined_df.drop(columns=["Placeholder"])
    combined_df = combined_df.dropna()

    combined_excel_file = "C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\data_src\\instock_data\\Genuis_Mobile.xlsx"
    combined_df.to_excel(combined_excel_file, index=False)

    os.remove(excel_file)

    print("Data has been combined, 'Placeholder' column removed, empty rows removed, and the original Excel file has been deleted.")

if __name__ == "__main__":
    main()
