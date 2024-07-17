import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Load the Excel file
file_path = 'C:\\Users\\savin\\OneDrive\\Desktop\\Projects\\Phone_price_compare\\data_src\\multiple_combined\\Combined_data.xlsx'
df = pd.read_excel(file_path)

# Streamlit app layout
st.title("Phone Price Comparison")

# Sidebar filters
st.sidebar.header("Filters")
selected_brands = st.sidebar.multiselect('Select Brands', df['Product Name'].apply(lambda x: x.split()[0]).unique())
selected_shops = st.sidebar.multiselect('Select Shops', df['shop'].unique())
price_range = st.sidebar.slider('Price Range', min_value=int(df['Price'].min()), max_value=int(df['Price'].max()), value=(int(df['Price'].min()), int(df['Price'].max())))
selected_storage = st.sidebar.multiselect('Select Storage (GB)', df['Storage'].dropna().unique())
selected_ram = st.sidebar.multiselect('Select RAM (GB)', df['RAM'].dropna().unique())

# Filter the dataframe
filtered_df = df[
    (df['Product Name'].apply(lambda x: x.split()[0]).isin(selected_brands) if selected_brands else True) &
    (df['shop'].isin(selected_shops) if selected_shops else True) &
    (df['Price'] >= price_range[0]) & (df['Price'] <= price_range[1]) &
    (df['Storage'].isin(selected_storage) if selected_storage else True) &
    (df['RAM'].isin(selected_ram) if selected_ram else True)
]

# Display the filtered data
st.write(f"Total results: {filtered_df.shape[0]}")
st.dataframe(filtered_df)

# # Create the SQLite engine and save filtered data to SQL
# engine = create_engine('sqlite:///data.db')
# filtered_df.to_sql('phonedb', con=engine, if_exists='replace', index=False)
#
# # Connect to the database and execute the query
# conn = engine.connect()
# query = 'SELECT * FROM phonedb'
# data = pd.read_sql(query, conn)
# conn.close()
#
# # Display the data in the main area
# st.dataframe(data)
