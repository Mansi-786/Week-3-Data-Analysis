import pandas as pd

# Load the sales dataset
df = pd.read_csv("sales_data.csv")

# Calculate total sales
total_sales = df["Total_Sales"].sum()

# Calculate average sales
average_sales = df["Total_Sales"].mean()

# Find highest sale
highest_sale = df["Total_Sales"].max()

# Find lowest sale
lowest_sale = df["Total_Sales"].min()

# Find best-selling product based on total quantity sold
product_sales = df.groupby("Product")["Quantity"].sum()

best_selling_product = product_sales.idxmax()
best_selling_quantity = product_sales.max()

# Display final sales analysis report
print("\n" + "=" * 45)
print("       SALES DATA ANALYSIS REPORT")
print("=" * 45)

print(f"Total Sales           : ₹{total_sales:,.2f}")
print(f"Average Sales         : ₹{average_sales:,.2f}")
print(f"Highest Sale          : ₹{highest_sale:,.2f}")
print(f"Lowest Sale           : ₹{lowest_sale:,.2f}")
print(f"Best-Selling Product  : {best_selling_product}")
print(f"Quantity Sold         : {best_selling_quantity}")

print("=" * 45)
