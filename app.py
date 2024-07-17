import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Load the Excel file
file_path = 'data_src/multiple_combined/Combined_data.xlsx'
df = pd.read_excel(file_path)

# Replace NaN values for RAM and Storage with '-'
df['RAM'] = df['RAM'].fillna('-')
df['Storage'] = df['Storage'].fillna('-')

# Convert RAM and Storage columns to integer format where possible
df['RAM'] = df['RAM'].apply(lambda x: '{:.0f}'.format(x) if x != '-' else x)
df['Storage'] = df['Storage'].apply(lambda x: '{:.0f}'.format(x) if x != '-' else x)

# Move 'Product Link' column to the last position
cols = [col for col in df.columns if col != 'Product Link'] + ['Product Link']
df = df[cols]

# Streamlit app layout
st.title("Phone Price Comparison")

# Sidebar filters
st.sidebar.header("Filters")
selected_brands = st.sidebar.multiselect('Select Brands', df['Product Name'].apply(lambda x: x.split()[0]).unique())
selected_shops = st.sidebar.multiselect('Select Shops', df['shop'].unique())
price_range = st.sidebar.slider('Price Range', min_value=int(df['Price'].min()), max_value=int(df['Price'].max()),
                                value=(int(df['Price'].min()), int(df['Price'].max())))
selected_storage = st.sidebar.multiselect('Select Storage (GB)', df['Storage'].unique())
selected_ram = st.sidebar.multiselect('Select RAM (GB)', df['RAM'].unique())

# Filter the dataframe
filtered_df = df[
    (df['Product Name'].apply(lambda x: x.split()[0]).isin(selected_brands) if selected_brands else True) &
    (df['shop'].isin(selected_shops) if selected_shops else True) &
    (df['Price'] >= price_range[0]) & (df['Price'] <= price_range[1]) &
    (df['Storage'].isin(selected_storage) if selected_storage else True) &
    (df['RAM'].isin(selected_ram) if selected_ram else True)
    ]

# Display the filtered data
# Display the filtered data without the index
st.write(f"Total results: {filtered_df.shape[0]}")
st.dataframe(
    filtered_df.reset_index(drop=True).style.format({'Price': 'Rs. {:,.0f}', 'RAM': '{} GB', 'Storage': '{} GB'}))
