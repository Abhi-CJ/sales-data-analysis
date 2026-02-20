# Sales & Profit Data Analysis Project

##  Project Overview

This project performs an end-to-end exploratory data analysis on retail transactional data to uncover **revenue trends, profitability drivers, customer behavior, regional performance, and discount impact**.

The objective is to move beyond basic aggregation and identify **actionable business insights**, including:

* High-revenue but low-profit products
* Discount-driven losses
* Customer purchasing patterns
* Regional and seasonal performance differences

---

## Dataset Description

The dataset consists of **380 retail transactions** with operational, financial, and customer-level information.

Key features include:

* **Order_ID** — Unique order identifier
* **Customer_ID & Customer_Name** — Customer tracking
* **Region & City** — Geographic performance analysis
* **Category & Product** — Product hierarchy
* **Quantity & Price** — Purchase details
* **Discount (%), Discount_Amount & Shipping_Cost** — Profitability factors
* **Order_Status & Payment_Mode** — Order lifecycle information
* **Total_Sales & Profit** — Core business metrics

---

## Tech Stack

* **Python**
* **Pandas** — Data cleaning, feature engineering, aggregation
* **NumPy** — Numerical operations
* **Matplotlib** — Visualization and trend analysis

---

## Data Cleaning & Feature Engineering

The following preprocessing steps were applied:

* Converted **Order_Date** to datetime format
* Extracted **Year, Month Name, and Month Number** features
* Removed **Cancelled orders** to avoid revenue distortion
* Filtered dataset (`sold_products`) to include only realized sales:

  * Excluded COD orders that were still **Pending or Shipped**
* Created derived metrics:

  * **Profit Margin**
  * **Profit Per Unit**
  * **Regional Revenue Contribution**

---

## Exploratory Analysis Performed

### Sales & Profit Trends

* Monthly revenue vs profit comparison
* Year-specific performance analysis (2024 vs 2025)

### Category & Product Analysis

* Category-wise revenue and profit contribution
* Loss-making products detection
* Product demand vs profitability evaluation

### Regional Performance

* Region-wise revenue and profit comparison
* Identification of **high-sales but low-profit region–product combinations**
* Top-performing cities by revenue

### Customer Behavior

* Customer segmentation (one-time vs repeat buyers)
* Average order value analysis
* Top customers by revenue, profit, and purchase quantity

### 💸 Discount Impact

* Discount vs profit correlation
* Identification of discount thresholds causing losses

---

## Key Business Insights

* Certain products generate strong revenue but weak profitability due to high discounts and shipping costs
* Repeat customers contribute disproportionately to profit stability
* Specific region–product combinations show **profit leakage despite high demand**
* Aggressive discounting directly correlates with loss-making transactions

---

## Visualizations Included

* Sales vs Profit scatter analysis
* Monthly Sales & Profit comparison charts
* Category Revenue vs Profit bar charts
* Regional Sales vs Profit distribution
* Discount vs Profit scatter analysis
* Region–Product performance scatter plot

---

## Conclusion

This project demonstrates how structured data analysis can uncover **hidden profitability risks, customer value patterns, and regional growth opportunities**.

The insights can support:

* Discount optimization
* Product pricing decisions
* Regional marketing strategy
* Customer retention planning

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

