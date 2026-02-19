                        
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("sales_data_380_rows_with_names.csv")

# Dataset overview
rows, columns = df.shape # (380, 17)
columns_list = df.columns
null_values = df.isnull().sum()
duplicate_values = df.duplicated().sum()

# Date Features
df['Order_Date'] = pd.to_datetime(df['Order_Date'], dayfirst=True)
df['Month'] = df['Order_Date'].dt.month_name()
df['Year'] = df['Order_Date'].dt.year
df['Month_num'] = df['Order_Date'].dt.month


total_years = df['Year'].unique()   # 2024 and 2025 (onty 14 data)

# ===================== Sold Products  =====================


sold_products = df[df['Order_Status'] != 'Cancelled']

#=========== Remove COD orders that are Pending or Shipped =============
mask = ~(
    (sold_products['Payment_Mode'] == 'Cash on Delivery') &
    ((sold_products['Order_Status'] == 'Pending') | (sold_products['Order_Status'] == 'Shipped'))
)

sold_products = sold_products[mask]





# ===================== OVerall Sales and profit =====================

overall_sales = sold_products['Total_Sales'].sum()
overall_profit = sold_products['Profit'].sum()
overall_profit_margin = overall_profit/overall_sales if overall_sales > 0 else 0
print(len(sold_products[sold_products['Year'] == 2025]  ))

#Over Sales and Profit Visualize 
plt.scatter(sold_products['Total_Sales'], sold_products['Profit'], alpha=0.6)

plt.xlabel('Sales')
plt.ylabel('Profit')
plt.title('Sales vs Profit Relationship')

plt.axhline(0, linestyle='--')
plt.show()




# ===================== Sales Performance Of Year 2024 =====================
# Sales in 2024 
total_sales = sold_products[sold_products['Year'] == 2024].groupby('Year')['Total_Sales'].sum()
total_profit = sold_products[sold_products['Year'] == 2024].groupby('Year')['Profit'].sum()




# ===================== Monthly SALES PERFORMANCE =====================
# ===================== Remove cancelled orders   =====================




monthly_sales = sold_products.groupby('Month_num')['Total_Sales'].sum()

monthly_sales_trend = monthly_sales.sort_index()
monthly_sales_ranking = monthly_sales.sort_values(ascending = False)

monthly_profit = sold_products.groupby('Month_num')['Profit'].sum()
monthly_profit_trend = monthly_profit.sort_index()
monthly_profit_ranking = monthly_profit.sort_values(ascending = False)



#Monthly sales trend vs profit trend


colors = [
    'red','blue','green','orange','purple','brown',
    'pink','gray','olive','cyan','gold','teal'
]

plt.figure(figsize = (7,3))
width = 0.40
months = monthly_sales_trend.index
x = np.arange(len(months))

plt.bar(x - width /2, monthly_sales_trend.values, color = 'skyblue', label = 'Sales')
plt.bar(x + width /2, monthly_profit_trend.values, color = 'gray', label = 'Profit')

plt.xlabel("Monthly Sales", fontsize = 15)
plt.ylabel('Profit', fontsize = 15)
plt.title('Sales Trend Vs Profit', fontsize = 18)

plt.legend()
month_labels = sold_products.groupby('Month_num')['Month'].first().sort_index()
plt.xticks(x, month_labels.values)

plt.show()









# ===================== CATEGORY ANALYSIS =====================
revenue_by_category = sold_products.groupby('Category')['Total_Sales'].sum().sort_values(ascending=False)
profit_by_category = sold_products.groupby('Category')['Profit'].sum()
average_revenue_by_category = sold_products.groupby('Category')['Total_Sales'].mean()



# Revenue and profit by category



categories = revenue_by_category.index
x = np.arange(len(categories))
width = 0.40

plt.figure(figsize = (10,6))

plt.bar(x - width/ 2, revenue_by_category.values, width, label ='Revenue', color = colors[10])
plt.bar(x + width/2 , profit_by_category.values, width, label = 'Profit',color = colors[5])

plt.xlabel('Category', fontsize = 18)
plt.ylabel('Amount', fontsize = 18)
plt.title('Revenue and Profit by Category', fontsize = 20)

plt.xticks(x, categories, rotation = 20,fontsize = 13)
plt.legend()
plt.show()





# Loss-making products by category
loss_making_products_by_category = (sold_products[sold_products['Profit'] < 0].groupby('Category').agg({'Quantity':'sum','Total_Sales':'sum','Profit':'sum'})).sort_values('Profit')










# ===================== REGIONAL ANALYSIS =====================



regional_revenue = sold_products.groupby('Region')['Total_Sales'].sum()
regional_revenue_ratio = regional_revenue/overall_sales

regional_profit = sold_products.groupby('Region')['Profit'].sum()
regional_profit_ratio = regional_profit /overall_profit
average_revenue_by_region = sold_products.groupby('Region')['Total_Sales'].mean()


profit_margin_by_category = profit_by_category / revenue_by_category.replace(0,1) 
profit_margin_by_region = regional_profit / regional_revenue.replace(0,1)


# Regional revenue

plt.bar(regional_revenue.index, regional_revenue.values, color = colors[2:6])
plt.xlabel('Regions', fontsize = 15)
plt.ylabel('Revenue', fontsize = 15)
plt.title('Regional sales', fontsize = 17)
plt.show()


#Regional Profit

plt.bar(regional_profit.index, regional_profit.values, color = colors[4:8])
plt.xlabel('Regions', fontsize = 15)
plt.ylabel('Profit', fontsize = 15)
plt.title('Regional Profit', fontsize = 17)
plt.show()



#Regions with  sales higher than average  sales  but lower profit than average profit 
region_analysis = sold_products.groupby(['Region','Product']).agg({
    'Total_Sales':'sum',
    'Profit':'sum'
})

high_sales_low_profit = region_analysis[
    (region_analysis['Total_Sales'] > region_analysis['Total_Sales'].mean()) &
    (region_analysis['Profit'] < region_analysis['Profit'].mean())
]






plt.figure(figsize=(12,7))

avg_sales = region_analysis['Total_Sales'].mean()
avg_profit = region_analysis['Profit'].mean()

for idx in region_analysis.index:
    
    sales = region_analysis.loc[idx, 'Total_Sales']
    profit = region_analysis.loc[idx, 'Profit']
    
    # Highlight high sales but low profit
    if idx in high_sales_low_profit.index:
        plt.scatter(sales, profit)
    else:
        plt.scatter(sales, profit)
    
    # Label as Region-Product
    label = f"{idx[0]}-{idx[1]}"
    plt.text(sales, profit, label, fontsize=8)

# Average reference lines
plt.axvline(avg_sales, linestyle='--')
plt.axhline(avg_profit, linestyle='--')

plt.xlabel('Total Sales', fontsize=12)
plt.ylabel('Total Profit', fontsize=12)
plt.title('Region-Product Performance: Sales vs Profit', fontsize=14)

plt.tight_layout()
plt.show()



# Top cities
top_3_cities_by_sales = (
    sold_products.groupby(['Region','City']).agg({'Total_Sales': 'sum', 'Discount (%)': 'mean','Profit': 'sum'})
          .sort_values(['Region','Total_Sales'], ascending=[True,False])
      .groupby('Region').head(3)
)









# ===================== ORDER HEALTH =====================
total_orders = df['Order_ID'].nunique()
product_order_status = df.groupby('Order_Status')['Quantity'].sum()
total_quantity = product_order_status.sum()
product_order_status_ratio = product_order_status/total_quantity
print(product_order_status_ratio)



plt.figure(figsize = (10,8))
product_order_status.plot(kind = 'bar', color = ['red','green', 'yellow','pink'])

plt.ylabel('Product Count', fontsize = 17)
plt.title('Order Status Of Products', fontsize = 17)
plt.show()





cancellation_rate = df[df['Order_Status']=='Cancelled']['Order_ID'].nunique() / total_orders
delivered_rate = df[df['Order_Status']=='Delivered']['Order_ID'].nunique() / total_orders
pending_rate = df[df['Order_Status']=='Pending']['Order_ID'].nunique() / total_orders

cancellation_by_payment = (
    df[df['Order_Status']=='Cancelled'].groupby('Payment_Mode')['Order_ID'].nunique()
    / df.groupby('Payment_Mode')['Order_ID'].nunique()
)




cancellation_by_region_order_status = (
    df[df['Order_Status'] == 'Cancelled']
      .groupby(['Region','Payment_Mode'])['Order_ID'].nunique()
      / df.groupby(['Region','Payment_Mode'])['Order_ID'].nunique()
)

# order_region_payment_corr = df[['Region', 'Payment_Mode', 'Order_Status']].corr()








# ===================== CUSTOMER ANALYSIS =====================
unique_customers = df['Customer_ID'].nunique()

customer_segmentation = (
    df.groupby(['Customer_ID','Product'])
      .agg({'Total_Sales':'sum','Profit':'sum'})
      .sort_values('Total_Sales',ascending=False)
)

average_order_value = sold_products.groupby('Customer_ID')['Total_Sales'].mean()
order_frequency = df.groupby('Customer_ID')['Order_Date'].nunique()

regular_customers = order_frequency[order_frequency>1]
one_time_customers = order_frequency[order_frequency==1]

top_5_customers = (
    sold_products.groupby(['Customer_ID','Product'])
      .agg({'Total_Sales':'sum', 'Profit':'sum'})
      .sort_values('Profit',ascending=False)
      .head(5)
)

customer_avg_sales_profit = sold_products.groupby('Customer_ID').agg({'Total_Sales':'mean','Profit':'mean'})
customer_avg_sales_profit_corr = customer_avg_sales_profit.corr()








# ===================== PRODUCT ANALYSIS =====================
product_demand_profit = sold_products.groupby('Product').agg({'Quantity':'sum','Profit':'sum'})
monthly_product_demand_profit = sold_products.groupby(['Product','Month']).agg({'Quantity':'sum','Total_Sales':'sum','Profit':'sum'})
loss_making_products = sold_products[sold_products['Profit']<0].groupby('Product').agg({'Quantity':'sum','Total_Sales':'sum','Profit':'sum'})

price_shipping_discount_sales_profit_corr = df[['Price','Shipping_Cost','Discount (%)','Total_Sales','Profit']].corr()







# ===================== DISCOUNT ANALYSIS =====================
discounted_products_count = df[df['Discount (%)']>0]['Quantity'].sum()
discount_loss = df[df['Profit'] < 0 ].groupby('Discount (%)')['Profit'].sum()
discount_vs_profit = df.groupby('Discount (%)')['Profit'].sum()
discount_profit_corr = df[['Discount (%)','Profit']].corr()


#Disocunt vs Profit


plt.figure(figsize = (8,5))
plt.scatter(df['Discount (%)'], df['Profit'], c = [i for i in (df['Profit'])] , cmap = 'coolwarm', label = 'Profit')

plt.xlabel('Percentage Discount', fontsize = 15)
plt.ylabel('Profit', fontsize = 15)
plt.title('Dicount Impact on Profit', fontsize = 17)

color_bar = plt.colorbar()
color_bar.set_label('Profit Level', fontsize = 15)
plt.legend()

plt.show()

# ===================== PRICE & PROFIT RELATION =====================
shipping_price_profit_corr = df[['Shipping_Cost','Price','Profit']].corr()
price_discount_profit_corr = df[['Price','Discount (%)','Profit']].corr()







# ===================== FINAL PRODUCT PERFORMANCE =====================
df['Profit_Per_Unit'] = df['Profit'] / df['Quantity'].replace(0,1)

product_sales_profit_analysis = (
    df.groupby('Product')
      .agg({'Quantity':'sum','Total_Sales':'sum','Discount (%)':'mean','Profit':'sum','Profit_Per_Unit':'mean'})
      .sort_values('Quantity',ascending=False)
)
             
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
