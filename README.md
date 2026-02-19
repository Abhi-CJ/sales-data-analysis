

# 📊 Sales & Profit Data Analysis Project

## Project Overview

This project analyzes retail sales data to identify revenue trends, profit patterns, customer purchasing behavior, order frequency, and seasonality.

The analysis focuses on high-performing regions, cities, and identifying products and region–product combinations generating high sales but low profit.

---

## Dataset Description

The dataset contains the following transactional retail data:

* **Order_ID** — Unique identifier for each order
* **Customer_ID** — Unique identifier for each customer
* **Region, City** — Geographical information
* **Category, Product** — Product classification
* **Shipping_Cost, Discount (%), Discount_Amount** — Cost factors affecting profitability
* **Order_Status, Payment_Mode** — Operational details
* **Quantity, Price** — Purchase details
* **Total_Sales, Profit** — Financial performance metrics
* **Customer_Name** — Customer identification

---

## Tools & Technologies

* **Python**
* **NumPy** — Numerical computation
* **Pandas** — Data cleaning and aggregation
* **Matplotlib** — Data visualization

---

## Data Cleaning Steps

1. Converted **Order_Date** to datetime format

2. Extracted **Year, Month, and Month Number** features

3. Removed **Cancelled orders** for accurate revenue calculation

4. Created a filtered dataset called **sold_products**:

   * Removed cancelled orders
   * Excluded Cash-on-Delivery orders that were still **Pending or Shipped**
   * Ensured only realized sales were used for revenue and profit analysis

5. Created derived metrics such as:

   * Profit Margin
   * Profit Per Unit

---

## Exploratory Data Analysis

* Monthly revenue and profit trend analysis
* Category-wise revenue and profitability contribution
* Identification of peak sales months
* Regional revenue and profit comparison
* Detection of **high-sales but low-profit region–product combinations**
* Discount impact on profit and loss generation
* Product demand vs profitability analysis
* Top cities contributing to revenue
* Customer segmentation (one-time vs repeat customers)

---

## Key Business Insights

* Identification of revenue-driving categories with lower profit margins
* Detection of discount levels contributing to loss-making orders
* Regions and products generating high revenue but weak profitability
* Customer purchasing behavior and repeat purchase patterns

---

## Visualizations

The project includes multiple visualizations such as:

* Sales vs Profit scatter analysis
* Monthly Sales and Profit comparison charts
* Category Revenue vs Profit bar charts
* Regional sales and profit distribution
* Discount vs Profit scatter analysis
* Region–Product performance scatter plot

---

## Conclusion

This analysis highlights important business drivers affecting revenue and profitability, including discount strategy, regional performance, and product demand behavior.


