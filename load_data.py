                        
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("sales_data_380_rows_with_names.csv")

# Dataset overview
rows, columns = df.shape # (380, 17)
columns_list = df.columns
null_values = df.isnull().sum()
duplicate_values = df.duplicated().sum()

print('Data Overview')
print(f'\n Rows and Columns\n{rows} rows and  {columns} columns')
print(f'\nColumn Names\n{columns_list}')
print(f'\nTotal null values in dataset\n{null_values.sum()}')
print(f'\nTotal Duplicate Values in dataset\n{duplicate_values}')


# Date Features
df['Order_Date'] = pd.to_datetime(df['Order_Date'], dayfirst=True)
df['Month'] = df['Order_Date'].dt.month_name()
df['Year'] = df['Order_Date'].dt.year
df['Month_num'] = df['Order_Date'].dt.month
month_names = df['Month'].unique()
#Total years of data
total_years = df['Year'].unique()   # 2024 and 2025 (onty 14 data)



# ===================== ORDER HEALTH =====================

order_status = df.groupby('Order_Status')['Quantity'].sum()
total_orders = order_status.sum()
product_order_status_ratio = order_status/total_orders
print(product_order_status_ratio)


#Product Distribution by Order Status

plt.figure(figsize = (10,8))
plt.pie(order_status, labels = product_order_status_ratio.index, autopct = '%0.2f%%', colors = ['red','green', 'yellow','pink'], radius = 1.0)

plt.title('Product Distribution by Orders Status', fontsize = 17)
plt.show()




cancellation_rate = df[df['Order_Status']=='Cancelled']['Quantity'].sum() / total_orders
delivered_rate = df[df['Order_Status']=='Delivered']['Quantity'].sum() / total_orders
pending_rate = df[df['Order_Status']=='Pending']['Quantity'].sum() / total_orders

cancellation_by_payment = (
    df[df['Order_Status']=='Cancelled'].groupby('Payment_Mode')['Order_ID'].nunique()
    / df.groupby('Payment_Mode')['Order_ID'].nunique()
)


cancellation_by_region_order_status = (
    df[df['Order_Status'] == 'Cancelled']
      .groupby(['Region','Payment_Mode'])['Order_ID'].nunique()
      / df.groupby(['Region','Payment_Mode'])['Order_ID'].nunique()
)



# payment mode Preference

payment_mode_distribution = df['Payment_Mode'].value_counts()

plt.figure(figsize = (7,4))
plt.pie(payment_mode_distribution.values, labels =payment_mode_distribution.index,autopct = '%0.2f%%', colors = ['red','green', 'yellow','pink'], radius = 1.0 )  
plt.title('Payment mode Preference ', fontsize = 17)

plt.show()


#=============== January month sales performance in 2024 vs 2025===============

jan_sales_summary = df[df['Month'] == 'January'].groupby('Year').agg( {"Quantity":'sum','Total_Sales':'sum', 'Profit': 'sum'})

print(f'\nJanuary Month Sales in Year 2024 vs 2025\n{jan_sales_summary}')





# ===================== Remove biased data(year 2025)   =====================

df = df[df['Year'] != 2025] #Excluding year 2025 data because its very less only 14 data out of 234 


# ===================== Remove cancelled orders from total orders of year  2024  =====================


sold_products = df[df['Order_Status'] != 'Cancelled']

#=========== Remove COD orders that are Pending or Shipped =============
mask = ~(
    (sold_products['Payment_Mode'] == 'Cash on Delivery') &
    ((sold_products['Order_Status'] == 'Pending') | (sold_products['Order_Status'] == 'Shipped'))
)


# ===================== Sold Products  =====================

sold_products = sold_products[mask].copy()

unique_customers = sold_products['Customer_ID'].nunique()
remove_orders = len(df) - len(sold_products)

print(f'\nTotal orders\n{len(df)}' )
print(f'\nSold Products\n{len(sold_products)}')
print(f'\nRemoved Products\n{remove_orders}')






# ===================== Sales Performance Of Year 2024 =====================


# Calculate revenue, profit, and profit margin
revenue_2024 = sold_products['Total_Sales'].sum()
profit_2024 = sold_products['Profit'].sum()
profit_margin_2024 = profit_2024 / revenue_2024 if revenue_2024 > 0 else 0


# Visualization of sales performance in year 2024 
plt.scatter(sold_products['Total_Sales'], sold_products['Profit'], alpha = 0.6)

plt.xlabel('Sales')
plt.ylabel('Profit')
plt.title('Sales Performance in year 2024')

plt.axhline(0, linestyle = '--')
plt.show()







# =================== Monthly SALES PERFORMANCE OF YEAR 2024 ==================


monthly_sales = sold_products.groupby('Month_num')['Total_Sales'].sum()

monthly_sales_trend = monthly_sales.sort_index()
monthly_sales_ranking = monthly_sales.sort_values(ascending = False)

monthly_profit = sold_products.groupby('Month_num')['Profit'].sum()
monthly_profit_trend = monthly_profit.sort_index()
monthly_profit_ranking = monthly_profit.sort_values(ascending = False)

monthly_product_sold = sold_products.groupby('Month_num')['Quantity'].sum()



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
category_summary = sold_products.groupby('Category').agg({
    
    'Quantity': 'sum',
    'Total_Sales': 'sum',
    'Discount (%)': 'mean',
    'Profit': 'sum',
     
        }) 




category_summary['Profit_Margin (%)'] = category_summary['Profit'] / category_summary['Total_Sales'] * 100
print(f'\nCategory Wise Sales Performance\n{category_summary}')


#Visualization of revenue and profit contribution of each category

categories = category_summary.index
x = np.arange(len(categories))
width = 0.40

plt.figure(figsize = (10,6))

plt.bar(x - width/ 2, category_summary['Total_Sales'].values, width, label ='Revenue', color = colors[10])
plt.bar(x + width/2 , category_summary['Profit'].values, width, label = 'Profit',color = colors[5])

plt.xlabel('Category', fontsize = 18)
plt.ylabel('Amount', fontsize = 18)
plt.title('Revenue and Profit by Category', fontsize = 20)

plt.xticks(x, categories, rotation = 20,fontsize = 13)
plt.legend()
plt.show()





# ===================== REGIONAL ANALYSIS =====================
region_analysis = sold_products.groupby(['Region','Product']).agg({
    'Total_Sales':'sum',
    'Profit':'sum'
    
})

regional_profit_margin = region_analysis['Profit'] / region_analysis['Total_Sales']

average_revenue_by_region = sold_products.groupby('Region')['Total_Sales'].mean()

#Regional revenue and profit contribution in total revenue and profit

regional_revenue_ratio = region_analysis['Total_Sales']/revenue_2024    *100
regional_profit_ratio = region_analysis['Profit']/profit_2024 * 100





#Regional  Revenue vs Profit Visualization

width = 0.30
regions = region_analysis.index
x = np.arange(len(regions))

plt.bar(x - width / 2, region_analysis['Total_Sales'].values, color = 'orange', label = 'Sales')
plt.bar(x + width/ 2, region_analysis['Profit'].values, color = 'purple', label = 'Profit')


plt.xlabel("Region", fontsize = 15)
plt.ylabel("Amount", fontsize = 15)
plt.title("Regional Revenue vs Profit", fontsize = 17)
plt.legend()
plt.xticks(x, regions)
plt.show()




#Regions with  sales higher than average  sales  but lower profit 


high_sales_low_profit = region_analysis[
    (region_analysis['Total_Sales'] > region_analysis['Total_Sales'].mean()) &
    (region_analysis['Profit'] < region_analysis['Profit'].median())
]






plt.figure(figsize=(12,7))

avg_sales = region_analysis['Total_Sales'].mean()
avg_profit = region_analysis['Profit'].mean()

for idx in region_analysis.index:
    
    sales = region_analysis.loc[idx, 'Total_Sales']
    profit = region_analysis.loc[idx, 'Profit']
    
    # Highlight high sales but low profit
    if idx in high_sales_low_profit.index:
        plt.scatter(sales, profit, color='red', alpha=0.7)
    else:
        plt.scatter(sales, profit, color='gray', alpha=0.4)
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










# ===================== CUSTOMER ANALYSIS =====================
customer_count = sold_products['Customer_ID'].nunique()
customer_order_count = sold_products.groupby('Customer_ID')['Order_ID'].count()

order_frequency = df.groupby('Customer_ID')['Order_ID'].nunique()
average_order_value = sold_products.groupby('Customer_ID')['Total_Sales'].mean()

regular_customers = order_frequency[order_frequency>1]
one_time_customers = order_frequency[order_frequency==1]





#Sales Permormance metrics by each customer

Sales_by_each_customer = (
    sold_products.groupby('Customer_ID')
      .agg({'Total_Sales':'sum','Profit':'sum',})
      .sort_values('Total_Sales',ascending=False)
)
#Top 5 customers 
top_5_customers = Sales_by_each_customer.sort_values('Total_Sales',ascending=False).head(5)

print("\nTop 5 Customers:\n ",top_5_customers)











customer_avg_sales_profit = sold_products.groupby('Customer_ID').agg({'Total_Sales':'mean','Profit':'mean'})
customer_avg_sales_profit_corr = customer_avg_sales_profit.corr()






# ===================== PRODUCT ANALYSIS =====================
product_demand = sold_products.groupby('Product').agg({'Quantity':'sum','Total_Sales': 'sum','Profit':'sum'})
monthly_product_demand_profit = sold_products.groupby(['Product','Month']).agg({'Quantity':'sum','Total_Sales':'sum','Profit':'sum'})
loss_making_products = sold_products[sold_products['Profit']<0].groupby('Product').agg({'Quantity':'sum','Total_Sales':'sum','Profit':'sum'})

corr_matrix = sold_products[['Price','Discount (%)','Quantity','Profit']].corr()



plt.figure(figsize=(8,6))

# Display the correlation matrix as a heatmap
plt.imshow(corr_matrix, cmap='coolwarm', interpolation='nearest')

# Add colorbar
plt.colorbar(label='Correlation Coefficient')

# Set ticks and labels
columns = ['Price','Discount (%)','Quantity','Profit']
plt.xticks(range(len(columns)), columns, rotation=45, ha='right')
plt.yticks(range(len(columns)), columns)

# Add correlation values inside each cell
for i in range(len(columns)):
    for j in range(len(columns)):
        plt.text(j, i, f"{corr_matrix.iloc[i, j]:.2f}", ha='center', va='center', color='black')

plt.title('Correlation Heatmap (Price, Discount, Quantity, Profit)')
plt.tight_layout()
plt.show()




#Top 3 selling products 

top_3_selling_products = product_demand['Total_Sales'].sort_values(ascending = False).head(3)
print(top_3_selling_products)


# Top 3 demanding products

top_3_demanding_products = product_demand['Quantity'].sort_values(ascending = False).head(3)
print(top_3_demanding_products)

plt.bar(top_3_demanding_products.index, top_3_demanding_products.values, color = colors[5: 8])
plt.xticks(rotation=25)
plt.title("Top 3 Products by Demand")
plt.show()





# ===================== DISCOUNT ANALYSIS =====================


total_sold_products = sold_products['Quantity'].sum()
discounted_products_count = sold_products[sold_products['Discount (%)']>0]['Quantity'].sum()
products_without_discount = total_sold_products - discounted_products_count

print('Total Sold Products:', total_sold_products)
print('discounted_products_count',discounted_products_count)
print('Without Discount Products Total: ', products_without_discount)

#Discount and Profit Relation

discount_profit_corr = sold_products[['Discount (%)','Profit']].corr()


plt.figure(figsize = (8,5))
plt.scatter(sold_products['Discount (%)'], sold_products['Profit'], c = [i for i in (sold_products['Profit'])] , cmap = 'coolwarm', label = 'Profit')

plt.xlabel('Percentage Discount', fontsize = 15)
plt.ylabel('Profit', fontsize = 15)
plt.title('Discount Impact on Profit', fontsize = 17)

color_bar = plt.colorbar()
color_bar.set_label('Profit Level', fontsize = 15)
plt.legend()

plt.show()







# ===================== FINAL PRODUCT PERFORMANCE =====================
sold_products['Profit_Per_Unit'] = sold_products['Profit'] / sold_products['Quantity'].replace(0,1)

product_performance_analysis = (
    sold_products.groupby('Product')
      .agg({'Quantity':'sum','Total_Sales':'sum','Discount (%)':'mean','Profit':'sum','Profit_Per_Unit':'mean'})
      .sort_values('Quantity',ascending=False)
)

print(f'\nProduct Performance Metrics\n{product_performance_analysis}')             
                          
                         
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
