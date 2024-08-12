import pandas as pd

# Load the data with appropriate encoding
customers = pd.read_csv("C:\\Users\\arund\\Downloads\\Customers.csv", encoding='latin1')
sales = pd.read_csv("C:\\Users\\arund\\Downloads\\Sales.csv", encoding='latin1')
products = pd.read_csv("C:\\Users\\arund\\Downloads\\Products.csv", encoding='latin1')
stores = pd.read_csv("C:\\Users\\arund\\Downloads\\Stores.csv", encoding='latin1')
exchange_rates = pd.read_csv("C:\\Users\\arund\\Downloads\\Exchange_Rates.csv", encoding='latin1')

# Ensure proper datetime formats
sales['Order Date'] = pd.to_datetime(sales['Order Date'])
exchange_rates['Date'] = pd.to_datetime(exchange_rates['Date'])
customers['Birthday'] = pd.to_datetime(customers['Birthday'])

# Step 1: Merge Sales and Product Data
sales_products_merged = pd.merge(sales, products, on='ProductKey', how='inner')

# Step 2: Merge the Resulting Data with Customer Data
sales_products_customers_merged = pd.merge(sales_products_merged, customers, on='CustomerKey', how='left')

# Step 3: Merge with Store Data
sales_products_customers_stores_merged = pd.merge(sales_products_customers_merged, stores, on='StoreKey', how='left')

# Step 4: Merge with Exchange Rate Data
sales_products_customers_stores_exchange_merged = pd.merge(
    sales_products_customers_stores_merged, 
    exchange_rates, 
    left_on=['Order Date', 'Currency Code'], 
    right_on=['Date', 'Currency'], 
    how='left'
)

# Handle column name conflicts by renaming or dropping columns
sales_data = sales_products_customers_stores_exchange_merged.rename(columns={
    'State_x': 'Customer State',
    'Country_x': 'Customer Country',
    'State_y': 'Store Country',
    'Country_y': 'Store State'
})

# Drop the redundant 'Date' column from the sales_data dataframe
sales_data = sales_data.drop(columns=['Date'])

# Remove the dollar sign from `Unit Price USD` and convert to float
sales_data['Unit Price USD'] = sales_data['Unit Price USD'].replace(r'[\$,]', '', regex=True).astype(float)

# Remove the dollar sign from `Unit Cost USD` and convert to float
sales_data['Unit Cost USD'] = sales_data['Unit Cost USD'].replace(r'[\$,]', '', regex=True).astype(float)

# Calculate age at the time of sale
sales_data['Age'] = (sales_data['Order Date'].dt.year - sales_data['Birthday'].dt.year) - (
    (sales_data['Order Date'].dt.month < sales_data['Birthday'].dt.month) | 
    ((sales_data['Order Date'].dt.month == sales_data['Birthday'].dt.month) & 
     (sales_data['Order Date'].dt.day < sales_data['Birthday'].dt.day))
)

# Calculate Revenue in Local Currency
sales_data['Revenue in Local Currency'] = sales_data['Quantity'] * sales_data['Unit Price USD'] * sales_data['Exchange']

# Calculate Total Revenue in USD by converting back from Local Currency
sales_data['Total Revenue in USD'] = sales_data['Revenue in Local Currency'] / sales_data['Exchange']

# Step 5: Create the desired format
formatted_data = pd.DataFrame({
    'Sales ID': sales_data['Order Number'],
    'Customer ID': sales_data['CustomerKey'],
    'Product ID': sales_data['ProductKey'],
    'Product Name': sales_data['Product Name'],
    'Category': sales_data['Category'],
    'Subcategory': sales_data['Subcategory'],
    'Quantity Sold': sales_data['Quantity'],
    'Unit Cost USD': sales_data['Unit Cost USD'],  
    'Unit Price USD': sales_data['Unit Price USD'], 
    'Revenue': sales_data['Quantity'] * sales_data['Unit Price USD'],
    'Revenue in Local Currency': sales_data['Revenue in Local Currency'],
    'Store ID': sales_data['StoreKey'],
    'Store Location': sales_data['Store State'] + ', ' + sales_data['Store Country'],
    'Sale Date': sales_data['Order Date'].dt.strftime('%Y-%m-%d'),
    'Currency': sales_data['Currency Code'],
    'Exchange Rate': sales_data['Exchange'],
    'Gender': sales_data['Gender'],
    'Age': sales_data['Age'],
    'Location (city, state, country)': sales_data['City'] + ', ' + sales_data['Customer State'] + ', ' + sales_data['Customer Country']
})

# Format the `Revenue` columns to two decimal places
formatted_data['Revenue'] = formatted_data['Revenue'].round(2)
formatted_data['Revenue in Local Currency'] = formatted_data['Revenue in Local Currency'].round(2)
formatted_data['Unit Cost USD'] = formatted_data['Unit Cost USD'].round(2)
formatted_data['Unit Price USD'] = formatted_data['Unit Price USD'].round(2)

# View the formatted data
print(formatted_data.head())

# Save the formatted data to a new CSV file (if needed)
formatted_data.to_csv("C:\\Users\\arund\\Downloads\\sales_data.csv", index=False)
