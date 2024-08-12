import mysql.connector
import csv

# Connect to MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="data_spark"
)

cursor = mydb.cursor()

# Step 1: Create a table with sale_date as VARCHAR
create_table_query = """
CREATE TABLE IF NOT EXISTS sales_data (
    sales_id INT,
    customer_id INT,
    product_id INT,
    product_name VARCHAR(255),
    category VARCHAR(255),
    subcategory VARCHAR(255),
    quantity_sold INT,
    unit_cost_usd FLOAT,
    unit_price_usd FLOAT,
    revenue FLOAT,
    revenue_in_local_currency FLOAT,
    store_id INT,
    store_location VARCHAR(255),
    sale_date VARCHAR(10),  -- Store the date as VARCHAR(10)
    currency VARCHAR(10),
    exchange_rate FLOAT,
    gender VARCHAR(10),
    age INT,
    location VARCHAR(255)
)
"""

cursor.execute(create_table_query)
mydb.commit()

# Step 2: Insert data from the CSV file into the table
csv_file_path = "D:\\project_data_spark\\pandas\\data.csv"

with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader) 
    for row in csv_reader:
        sale_date = row[13]
        
        cursor.execute("""
            INSERT INTO sales_data (
                sales_id, customer_id, product_id, product_name, category, 
                subcategory, quantity_sold, unit_cost_usd, unit_price_usd, 
                revenue, revenue_in_local_currency, store_id, store_location, 
                sale_date, currency, exchange_rate, gender, age, location
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],
            row[8], row[9], row[10], row[11], row[12], sale_date, row[14],
            row[15], row[16], row[17], row[18]
        ))
    mydb.commit()

# Close the connection
cursor.close()
mydb.close()
