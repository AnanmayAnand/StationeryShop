import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv(r"D:\Python\StationeryShop\Stationary_Shop.csv")

# Clean data
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna()

# Calculate Total Sales
df['Total_Sales'] = df['Quantity_Sold'] * df['Unit_Price']

# Group data for plots
sales_by_category = df.groupby('Category')['Total_Sales'].sum()
sales_by_date = df.groupby('Date')['Total_Sales'].sum()

# Create subplots - 1 row, 3 columns
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# 1. Bar chart
sales_by_category.plot(kind='bar', ax=axes[0], color='skyblue')
axes[0].set_title('Total Sales by Category')
axes[0].set_ylabel('Total Sales')

# 2. Pie chart
sales_by_category.plot(kind='pie', ax=axes[1], autopct='%1.1f%%', startangle=90, shadow=True)
axes[1].set_ylabel('')
axes[1].set_title('Sales Distribution by Category')

# 3. Line chart
sales_by_date.plot(kind='line', ax=axes[2], marker='o', color='green')
axes[2].set_title('Total Sales Over Time')
axes[2].set_xlabel('Date')
axes[2].set_ylabel('Total Sales')
axes[2].grid(True)

plt.tight_layout()  # Adjust spacing so titles/labels don’t overlap
plt.show()
