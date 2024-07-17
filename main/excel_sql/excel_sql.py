import pandas as pd
from sqlalchemy import create_engine

# Define the path to the Excel file
excel_file_path = r'C:\Users\ADMIN\Desktop\Code\Phone_price_compare\data_src\multiple_combined\Combined_data.xlsx'

# Load the Excel file
df = pd.read_excel(excel_file_path)

# Define the desired column names (6 columns)
header = ['Shop', 'Product Name','Product Link', 'Price', 'RAM', 'Storage']

# Check the number of columns in your Excel data
if len(df.columns) != len(header):
    raise ValueError(f"Expected {len(header)} columns, but the Excel data has {len(df.columns)} columns.")

# Rename columns to match the desired column names
df.columns = header

# Define MySQL database connection parameters
db_host = 'localhost'  # Replace with your MySQL host address
db_user = 'root'  # Replace with your MySQL username
db_password = ''  # Replace with your MySQL password
db_name = 'phone'  # Replace with the name of your MySQL database

# Create a MySQL database connection using SQLAlchemy
engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}')

# Write the DataFrame to the database (replace 'table_name' with your desired table name)
table_name = 'phonedb'
df.to_sql(table_name, con=engine, if_exists='replace', index=False)

print(f"Data has been successfully formatted and saved to MySQL database '{db_name}'.")
