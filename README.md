# Sales & Profitability Data Analysis Project

## Project Overview

This project performs an **end-to-end business-driven analysis** on retail transactional data to uncover:

* Revenue and profitability trends
* Customer purchase behavior and retention
* Regional and category performance gaps
* Discount impact on profit margins
* Operational risks such as cancellations and payment failures

Unlike basic aggregation projects, this analysis applies **realistic business filtering** to evaluate only **realized revenue**, preventing misleading profitability insights.

The workflow mimics how real companies evaluate sales performance after removing operational noise.

---

## 🗂 Dataset Description

The dataset contains **380 retail transactions** with financial, operational, geographic, and customer attributes.

### Key Features

* **Order_ID** — Unique order identifier
* **Customer_ID & Customer_Name** — Customer tracking
* **Region & City** — Geographic segmentation
* **Category & Product** — Product hierarchy
* **Quantity, Price & Shipping_Cost** — Transaction metrics
* **Discount (%) & Discount_Amount** — Pricing strategy indicators
* **Order_Status & Payment_Mode** — Order lifecycle behavior
* **Total_Sales & Profit** — Core business performance metrics
* **Order_Date** — Used for time-series analysis

---

## 🛠 Tech Stack

* **Python**
* **Pandas** — Cleaning, aggregation, feature engineering
* **NumPy** — Numerical computation
* **Matplotlib** — Visualization and trend analysis

---

## Data Validation & Feature Engineering

### Dataset Quality Checks

* Shape and column inspection
* Null value detection
* Duplicate record identification

### Time-Based Feature Creation

* Converted **Order_Date** to datetime
* Extracted:

  * Month name
  * Month number
  * Year

This enabled time-series analysis and seasonal performance evaluation.

---

## Order Health & Operational Analysis

Performed **before filtering** to understand business funnel health:

* Product distribution across order statuses
* Cancellation rate analysis
* Cancellation patterns by payment mode and region
* Payment mode preference evaluation

This step highlights operational risks that directly affect realized revenue.

---

## Business Filtering (Core Strength of Project)

To ensure realistic profitability insights:

* Removed **2025 data** due to insufficient sample size
* Excluded **Cancelled orders**
* Removed **Cash-on-Delivery orders that were Pending or Shipped**

A clean dataset `sold_products` was created containing only **fulfilled and revenue-realized transactions**.

Key metrics derived:

* Total fulfilled orders
* Removed orders count
* Unique customers

---

## Sales Performance Analysis (2024)

* Total revenue and profit calculation
* Profit margin estimation
* Scatter visualization of sales vs profit
* Identification of loss-making transactions

---

## Monthly Performance Analysis

* Monthly revenue trend
* Monthly profit divergence
* Monthly demand distribution
* Sales vs profit bar comparison for seasonality detection

---

## Category Analysis

* Category-wise quantity, revenue, discount, and profit
* Profit margin comparison across categories
* Revenue vs profit visualization

This identifies **high-volume but low-margin categories**.

---

## Regional Analysis

* Region–product level revenue and profit aggregation
* Regional revenue and profit contribution ratios
* Detection of **high-sales but low-profit region-product combinations**
* Region-product scatter with quadrant interpretation
* Top 3 cities by revenue within each region

---

## Customer Behavior Analysis

* Unique customer count
* Order frequency segmentation (one-time vs repeat buyers)
* Average order value per customer
* Top customers by revenue and profit
* Customer sales vs profit correlation

---

## Product Analysis

* Product demand vs revenue comparison
* Loss-making product identification
* Monthly product demand tracking
* Top revenue vs top demand product comparison

A **Matplotlib heatmap** evaluates relationships between:

* Price
* Discount
* Quantity
* Profit

---

## Discount Impact Analysis

* Discounted vs non-discounted product volume comparison
* Discount vs profit correlation
* Profit-colored scatter visualization showing discount sensitivity

This highlights discount levels that lead to profit erosion.

---

## Final Product Performance Metrics

A comprehensive product table was created including:

* Total demand
* Revenue contribution
* Average discount
* Profit
* Profit per unit

This enables pricing and assortment optimization decisions.

---

## Key Business Insights

* High demand does not always translate to profitability
* Aggressive discounting creates measurable profit leakage
* Several region–product pairs show strong revenue but weak margins
* Repeat customers contribute significantly to revenue stability
* Cancellation and COD behavior can distort performance perception if not filtered

---

## Visualizations Included

* Order status distribution pie chart
* Payment preference analysis
* Sales vs profit scatter
* Monthly sales vs profit comparison
* Category revenue vs profit chart
* Region–product profitability scatter
* Discount vs profit visualization
* Correlation heatmap
* Top demand product comparison

---

## Business Value

This analysis supports decision-making in:

* Pricing and discount optimization
* Product portfolio improvement
* Regional marketing investment
* Customer retention strategy
* Operational risk monitoring

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
