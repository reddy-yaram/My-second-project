# ==========================
# SHOP SALES ANALYSIS SYSTEM
# ==========================

# Products Table
products = [
    {"product_id": 1, "product_name": "Rice", "category": "Grocery"},
    {"product_id": 2, "product_name": "Sugar", "category": "Grocery"},
    {"product_id": 3, "product_name": "Oil", "category": "Grocery"},
    {"product_id": 4, "product_name": "Milk", "category": "Dairy"}
]

# Sales Table
sales = [
    {"sale_id": 1, "product_id": 1, "month": "May", "quantity": 100, "price": 50},
    {"sale_id": 2, "product_id": 2, "month": "May", "quantity": 80, "price": 40},
    {"sale_id": 3, "product_id": 3, "month": "May", "quantity": 60, "price": 120},
    {"sale_id": 4, "product_id": 1, "month": "June", "quantity": 150, "price": 50},
    {"sale_id": 5, "product_id": 2, "month": "June", "quantity": 120, "price": 40},
    {"sale_id": 6, "product_id": 4, "month": "June", "quantity": 90, "price": 30}
]

# ==========================
# TRANSFORM DATA
# Add Revenue Column
# ==========================

for sale in sales:
    sale["revenue"] = sale["quantity"] * sale["price"]

# ==========================
# JOIN OPERATION
# Combine Product and Sales Tables
# ==========================

print("\nJOINED DATA")
print("-" * 50)

joined_data = []

for sale in sales:
    for product in products:

        if sale["product_id"] == product["product_id"]:

            row = {
                "product_name": product["product_name"],
                "month": sale["month"],
                "quantity": sale["quantity"],
                "price": sale["price"],
                "revenue": sale["revenue"]
            }

            joined_data.append(row)

            print(row)

# ==========================
# MONTHLY SALES CALCULATION
# ==========================

may_total = 0
june_total = 0

for sale in sales:

    if sale["month"] == "May":
        may_total += sale["revenue"]

    elif sale["month"] == "June":
        june_total += sale["revenue"]

# ==========================
# MONTH COMPARISON
# ==========================

print("\nMONTH COMPARISON")
print("-" * 50)

print("May Revenue :", may_total)
print("June Revenue:", june_total)

if june_total > may_total:
    print("Sales Increased in June")

elif june_total < may_total:
    print("Sales Decreased in June")

else:
    print("Sales Remained Same")

# ==========================
# GROWTH PERCENTAGE
# ==========================

growth = ((june_total - may_total) / may_total) * 100

print("Growth Percentage:", round(growth, 2), "%")

# ==========================
# PRODUCT-WISE SALES
# ==========================

product_sales = {}

for sale in sales:

    pid = sale["product_id"]

    if pid not in product_sales:
        product_sales[pid] = 0

    product_sales[pid] += sale["quantity"]

# ==========================
# BEST SELLING PRODUCT
# ==========================

best_product_id = max(product_sales, key=product_sales.get)

for product in products:
    if product["product_id"] == best_product_id:
        best_product_name = product["product_name"]

print("\nBest Selling Product:", best_product_name)

# ==========================
# LEAST SELLING PRODUCT
# ==========================

least_product_id = min(product_sales, key=product_sales.get)

for product in products:
    if product["product_id"] == least_product_id:
        least_product_name = product["product_name"]

print("Least Selling Product:", least_product_name)

# ==========================
# TOTAL REVENUE
# ==========================

total_revenue = 0

for sale in sales:
    total_revenue += sale["revenue"]

print("\nTotal Revenue:", total_revenue)

# ==========================
# AVERAGE REVENUE
# ==========================

average_revenue = total_revenue / len(sales)

print("Average Revenue Per Sale:", round(average_revenue, 2))

# ==========================
# FINAL REPORT
# ==========================

print("\n" + "=" * 50)
print("SHOP SALES REPORT")
print("=" * 50)

print("May Revenue               :", may_total)
print("June Revenue              :", june_total)
print("Growth Percentage         :", round(growth, 2), "%")
print("Total Revenue             :", total_revenue)
print("Average Revenue Per Sale  :", round(average_revenue, 2))
print("Best Selling Product      :", best_product_name)
print("Least Selling Product     :", least_product_name)

print("=" * 50)