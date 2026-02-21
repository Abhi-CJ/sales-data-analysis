# 📊 Sales & Profitability Data Analysis Project

## 🚀 Project Overview

This project performs an **end-to-end exploratory and business-focused analysis** on retail transactional data to uncover **revenue trends, profitability drivers, customer behavior, regional performance, and discount impact**.

Unlike basic aggregation projects, this analysis applies **real business logic filtering** to evaluate only *realized sales*, enabling more accurate profitability insights.

The project identifies:

* High-revenue but low-profit products
* Discount-driven losses
* Customer purchase behavior and retention patterns
* Regional performance gaps
* Operational risks such as cancellations and payment-related issues

---

## 📁 Dataset Description

The dataset contains **380 retail transactions** with operational, financial, geographic, and customer-level attributes.

### Key Features

* **Order_ID** — Unique order identifier
* **Customer_ID & Customer_Name** — Customer tracking
* **Region & City** — Geographic segmentation
* **Category & Product** — Product hierarchy
* **Quantity, Price & Shipping_Cost** — Transaction-level metrics
* **Discount (%) & Discount_Amount** — Pricing strategy indicators
* **Order_Status & Payment_Mode** — Order lifecycle and behavior
* **Total_Sales & Profit** — Core business performance metrics

---

## 🛠 Tech Stack

* **Python**
* **Pandas** — Data cleaning, feature engineering, aggregation
* **NumPy** — Numerical computations
* **Matplotlib** — Visualization and business trend analysis

---

## 🧹 Data Cleaning & Business Filtering

To ensure accurate business insights, the following preprocessing steps were applied:

* Converted **Order_Date** to datetime format
* Extracted **Year, Month Name, and Month Number** features
* Removed **Cancelled orders** to prevent revenue distortion
* Created a **`sold_products` dataset** containing only fulfilled transactions
* Excluded **Cash-on-Delivery orders that were Pending or Shipped**, ensuring analysis reflects realized revenue

### 📌 Derived Business Metrics

* Profit Margin (%)
* Profit Per Unit
* Regional Revenue Contribution
* Category Profitability

---

## 🔍 Exploratory Analysis Performed

### 📈 Sales & Profit Trends

* Overall sales vs profit relationship
* Year-specific performance comparison (2024 vs 2025)
* Monthly sales and profit divergence analysis
* January YoY comparison across years

---

### 🛍 Category & Product Analysis

* Category-wise revenue, discount, and profit evaluation
* Detection of **loss-making products**
* Separation of **top-demand vs top-revenue products**
* Profit-per-unit analysis to identify inefficient products

---

### 🌍 Regional Performance

* Region-wise revenue and profit comparison
* Identification of **high-sales but low-profit region–product combinations**
* Top-performing cities within each region
* Regional contribution to overall revenue and profitability

---

### 👥 Customer Behavior Analysis

* Customer segmentation (one-time vs repeat buyers)
* Average order value analysis
* Top customers by revenue, profit, and quantity purchased
* Customer-level profitability correlation

---

### 📦 Order Health & Operations

* Product distribution across order statuses
* Cancellation rate analysis
* Cancellation patterns by payment mode and region

---

### 💸 Discount & Pricing Impact

* Discount vs profit relationship analysis
* Identification of discount levels causing negative profitability
* Evaluation of discount contribution to total sold quantity

---

### 🔗 Correlation Analysis

A **Matplotlib-based correlation heatmap** was created to evaluate relationships between:

* Price
* Discount
* Quantity
* Profit

This helps understand pricing strategy effects on profitability.

---

## 📊 Visualizations Included

* Sales vs Profit scatter analysis
* Monthly Sales & Profit comparison charts
* Category Revenue vs Profit bar charts
* Regional Sales vs Profit distribution
* Discount vs Profit scatter with color mapping
* Region–Product performance scatter plot
* Correlation heatmap (Price, Discount, Quantity, Profit)

---

## 💡 Key Business Insights

* Certain products generate strong revenue but weak profitability due to high discounting and shipping costs
* Repeat customers contribute significantly to revenue stability and profit consistency
* Multiple region–product combinations show **profit leakage despite strong demand**
* Aggressive discounting demonstrates a measurable negative impact on profitability
* Demand-heavy products are not always the most profitable, indicating pricing optimization opportunities

---

## 🎯 Business Value

This analysis supports strategic decision-making in:

* Discount optimization and pricing strategy
* Product portfolio refinement
* Regional marketing investment
* Customer retention planning
* Operational risk reduction

---

## ▶️ How to Run

```bash
git clone https://github.com/Abhi-CJ/sales-data-analysis.git
cd sales-data-analysis
python analysis.py
```

---

## 👨‍💻 Author

**Abhishek Jain**
