# Sales & Profitability Data Analysis Project

## Project Overview

This project performs an **end-to-end business-driven retail analysis** to uncover revenue trends, operational risks, customer behavior, and profitability drivers.

Unlike basic EDA projects, this analysis applies **realistic business filtering** to evaluate only **fulfilled revenue**, preventing misleading insights caused by cancellations and incomplete COD orders.

---

## Dataset Description

The dataset contains **380 retail transactions** with customer, product, geographic, and financial attributes.

### Key Features

* Order_ID — unique order identifier
* Customer_ID — customer tracking
* Region & City — geographic segmentation
* Category & Product — product hierarchy
* Quantity, Price, Shipping_Cost — transaction metrics
* Discount (%) — pricing strategy indicator
* Order_Status & Payment_Mode — operational behavior
* Total_Sales & Profit — core business KPIs
* Order_Date — used for time analysis

---

## Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib

---

## Data Validation

Performed initial dataset quality checks:

* Shape and column inspection
* Null value detection
* Duplicate record analysis

---

## Feature Engineering

* Converted **Order_Date** to datetime
* Extracted Month name, Month number, and Year
* Enabled time-series trend analysis

---

## Order Health Analysis (Before Filtering)

This stage evaluates the operational funnel:

* Orders count by status
* Order status distribution pie chart
* Payment mode preference
* Cancellation patterns by payment mode and region

This helps understand how operational issues impact realized revenue.

---

## Business Filtering Logic (Core Project Strength)

To ensure realistic profitability insights:

* Removed **2025 data** due to extremely small sample size
* Excluded **Cancelled orders**
* Removed **Cash-on-Delivery orders that were Pending or Shipped**

A clean dataset **`sold_products`** was created containing only fulfilled revenue transactions.

### Derived Metrics

* Total fulfilled orders
* Removed order count
* Unique customers

---

## Sales Performance (2024)

* Total revenue and profit calculation
* Profit margin estimation
* Sales vs Profit scatter visualization
* Identification of loss-making transactions

---

## Monthly Performance Analysis

* Monthly revenue trend
* Monthly profit divergence
* Best revenue and worst profit month detection
* Sales vs profit grouped bar comparison

---

## Category Analysis

* Category-wise quantity, revenue, discount, and profit
* Profit margin comparison
* Revenue vs profit visualization

Helps identify **high-volume but weak-margin categories**.

---

## Regional Analysis

* Region-product level revenue and profit aggregation
* Regional contribution to total revenue and profit
* Detection of **high-sales but low-profit combinations**
* Quadrant-style scatter with average reference lines
* Top 3 cities by revenue per region

---

## Customer Behavior Analysis

* Unique customer count
* Repeat vs one-time customer segmentation
* Average order value per customer
* Top 5 customers by revenue
* Customer revenue contribution

---

## Product Analysis

* Product demand vs revenue comparison
* Monthly product demand tracking
* Top revenue vs top demand products

A Matplotlib heatmap was created to analyze correlation between:

* Price
* Discount
* Quantity
* Profit

---

## Discount Impact Analysis

* Discounted vs non-discounted demand comparison
* Weak margin product detection
* Discount vs profit scatter visualization

This highlights discount levels causing profit erosion.

---

## Final Product Performance Metrics

A consolidated product performance table includes:

* Total demand
* Revenue contribution
* Average discount
* Profit
* Profit per unit

Supports pricing and assortment optimization.

---

## Key Business Insights

* High demand does not guarantee profitability
* Discounting shows measurable profit leakage
* Some region-product combinations generate strong revenue but weak margins
* Repeat customers contribute significantly to revenue stability
* Operational filtering is critical to avoid misleading business conclusions

---

## Visualizations Included

* Order status distribution
* Payment mode preference
* Sales vs profit scatter
* Monthly sales vs profit comparison
* Category revenue vs profit chart
* Region-product profitability scatter
* Discount vs profit visualization
* Correlation heatmap
* Top demand product comparison

---

## How to Run

```bash
git clone https://github.com/Abhi-CJ/sales-data-analysis.git
cd sales-data-analysis
python analysis.py
```

---

## Author

**Abhishek Jain**
