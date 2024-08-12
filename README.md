# DataSpark: Illuminating Insights for Global Electronics

## Project Overview

**DataSpark: Illuminating Insights for Global Electronics** is a comprehensive data analytics project aimed at providing actionable recommendations for Global Electronics, a leading retailer of consumer electronics. The project leverages data from various sources, including customer, product, sales, store, and currency exchange rates, to uncover valuable insights that can enhance customer satisfaction, optimize operations, and drive overall business growth.

### Key Skills Demonstrated
- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Data Management using SQL
- Power BI/Tableau Visualizations
- Retail Analytics in the Electronics Industry

## Problem Statement

As part of Global Electronics' data analytics team, the task is to conduct a thorough Exploratory Data Analysis (EDA) on the company’s datasets. The goal is to derive insights that will help in refining marketing strategies, improving sales forecasting, optimizing inventory management, and guiding product and store decisions.

### Business Use Cases
1. Enhancing Marketing Strategies: Tailor campaigns based on customer demographics and purchasing behavior.
2. Optimizing Inventory Management: Identify trends and patterns to improve stock management.
3. Sales Forecasting: Analyze historical sales data to predict future trends.
4. Product Development: Identify popular and less popular products to guide product improvements.
5. Store Operations: Make data-driven decisions for store expansions and operational enhancements.
6. International Pricing Strategies: Understand the impact of currency exchange rates on sales.

## Approach

### 1. Data Cleaning and Preparation
- Handle missing values and ensure data integrity.
- Convert data types where necessary (e.g., dates, numerical values).
- Merge datasets to create a cohesive data structure for analysis.

### 2. Data Management using SQL
- Load the cleaned and prepared data into an SQL database.
- Create relevant tables for each dataset and use SQL INSERT statements to populate the database.

### 3. Power BI Visualization
- Connect the SQL database to Power BI/Tableau.
- Import data and create interactive dashboards to visualize key insights.

### 4. SQL Queries for Key Insights

The project includes a set of SQL queries designed to extract valuable insights from the data. These queries focus on customer analysis, sales analysis, product analysis, and store analysis.

### Customer Analysis

- **Demographic Distribution**: Analyze customer distribution based on gender, age, location, and continent.
    ```sql
    -- Gender Distribution
    SELECT 
        Gender, 
        COUNT(CustomerKey) AS NumberOfCustomers
    FROM 
        Customers
    GROUP BY 
        Gender;

    -- Age Distribution
    SELECT 
        FLOOR(DATEDIFF(YEAR, Birthday, CURDATE())/10)*10 AS AgeGroup,
        COUNT(CustomerKey) AS NumberOfCustomers
    FROM 
        Customers
    GROUP BY 
        AgeGroup;

    -- Location Distribution
    SELECT 
        City, State, Country, Continent, 
        COUNT(CustomerKey) AS NumberOfCustomers
    FROM 
        Customers
    GROUP BY 
        City, State, Country, Continent;
    ```

- **Purchase Patterns**: Identify purchasing patterns such as average order value, frequency of purchases, and preferred products.
    ```sql
    -- Average Order Value and Number of Purchases per Customer
    SELECT 
        CustomerKey,
        AVG(Revenue) AS AverageOrderValue,
        COUNT(OrderNumber) AS NumberOfPurchases
    FROM 
        Sales
    GROUP BY 
        CustomerKey;

    -- Purchase Frequency by Product
    SELECT 
        ProductName, 
        COUNT(OrderNumber) AS PurchaseFrequency
    FROM 
        Sales
    GROUP BY 
        ProductName;
    ```

- **Customer Segmentation**: Segment customers based on demographics and purchasing behavior to identify key customer groups.
    ```sql
    SELECT 
        Gender, 
        FLOOR(DATEDIFF(YEAR, Birthday, CURDATE())/10)*10 AS AgeGroup,
        AVG(Revenue) AS AverageOrderValue
    FROM 
        Customers
    INNER JOIN 
        Sales ON Customers.CustomerKey = Sales.CustomerKey
    GROUP BY 
        Gender, 
        AgeGroup;
    ```

### Sales Analysis

- **Overall Sales Performance**: Analyze total sales over time, identifying trends and seasonality.
    ```sql
    SELECT 
        DATE_FORMAT(OrderDate, '%Y-%m') AS Month, 
        SUM(Revenue) AS TotalSales
    FROM 
        Sales
    GROUP BY 
        Month;
    ```

- **Sales by Product**: Evaluate which products are the top performers in terms of quantity sold and revenue generated.
    ```sql
    SELECT 
        ProductName, 
        SUM(QuantitySold) AS TotalQuantitySold, 
        SUM(Revenue) AS TotalRevenue
    FROM 
        Sales
    GROUP BY 
        ProductName;
    ```

- **Sales by Store**: Assess the performance of different stores based on sales data.
    ```sql
    SELECT 
        StoreLocation, 
        SUM(Revenue) AS TotalSales
    FROM 
        Sales
    GROUP BY 
        StoreLocation;
    ```

- **Sales by Currency**: Examine how different currencies impact sales figures, considering exchange rates.
    ```sql
    SELECT 
        Currency, 
        SUM(RevenueInLocalCurrency) AS TotalSalesInLocalCurrency, 
        SUM(Revenue) AS TotalSalesInUSD
    FROM 
        Sales
    GROUP BY 
        Currency;
    ```

### Product Analysis

- **Product Popularity**: Identify the most and least popular products based on sales data.
    ```sql
    SELECT 
        ProductName, 
        COUNT(OrderNumber) AS PurchaseCount
    FROM 
        Sales
    GROUP BY 
        ProductName
    ORDER BY 
        PurchaseCount DESC;
    ```

- **Profitability Analysis**: Calculate profit margins for products by comparing unit cost and unit price.
    ```sql
    SELECT 
        ProductName, 
        SUM(QuantitySold) * (UnitPriceUSD - UnitCostUSD) AS TotalProfit
    FROM 
        Sales
    GROUP BY 
        ProductName;
    ```

- **Category Analysis**: Analyze sales performance across different product categories and subcategories.
    ```sql
    SELECT 
        Category, Subcategory, 
        SUM(Revenue) AS TotalRevenue
    FROM 
        Sales
    GROUP BY 
        Category, Subcategory;
    ```

### Store Analysis

- **Store Performance**: Evaluate store performance based on sales, size (square meters), and operational data (open date).
    ```sql
    SELECT 
        StoreLocation, 
        SUM(Revenue) AS TotalSales,
        SUM(SquareMeters) AS TotalSquareMeters,
        MIN(OpenDate) AS FirstOpenDate
    FROM 
        Stores
    INNER JOIN 
        Sales ON Stores.StoreKey = Sales.StoreKey
    GROUP BY 
        StoreLocation;
    ```

- **Geographical Analysis**: Analyze sales by store location to identify high-performing regions.
    ```sql
    SELECT 
        Country, 
        SUM(Revenue) AS TotalSales
    FROM 
        Sales
    GROUP BY 
        Country;
    ```

## Power BI Dashboard

The project includes an interactive Power BI dashboard that visualizes key insights extracted from the data. The dashboard provides a user-friendly interface for exploring customer demographics, sales performance, product popularity, and store operations.

## Project Deliverables

1. **Cleaned and Integrated Datasets**: Ready for analysis.
2. **SQL Queries**: For extracting key business insights.
3. **Power BI Dashboard**: For interactive data exploration and visualization.
4. **Comprehensive EDA Report**: Summarizing key findings and recommendations.

## Getting Started

To get started with the project:

1. Clone the repository:
    ```bash
    git clone https://github.com/arunachaladevaraj/DataSpark-Illuminating-Insights-for-Global-Electronics.git
    ```

2. Set up the SQL database and load the data using the provided SQL scripts.

3. Connect the database to Power BI to start exploring the visualizations.

---



