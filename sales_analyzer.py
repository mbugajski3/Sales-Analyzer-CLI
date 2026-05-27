import csv

file = open("sales.csv")
headers = next(file)
total_revenue = 0
total_quantity_sold = 0
order_count = 0
quantity_by_product = {}
revenue_by_product = {}
revenue_by_category = {}

for line in file:
    line = line.strip()
    columns = line.split(",")
    order_id = columns[0]
    date = columns[1]
    product = columns[2]
    category = columns[3]
    quantity = columns[4]
    price = columns[5]
    quantity = int(quantity)
    price = float(price)
    revenue = quantity * price
    total_revenue += revenue
    total_quantity_sold += quantity
    order_count += 1
    if product not in quantity_by_product:
        quantity_by_product[product] = 0
    quantity_by_product[product] += quantity

    if product not in revenue_by_product:
        revenue_by_product[product] = 0
    revenue_by_product[product] += revenue

    if category not in revenue_by_category:
        revenue_by_category[category] = 0
    revenue_by_category[category] += revenue

best_selling_product_name = list(quantity_by_product.keys())[0]
best_selling_product_quantity = quantity_by_product[best_selling_product_name]

top_revenue_product_name = list(revenue_by_product.keys())[0]
top_revenue_product_value = revenue_by_product[top_revenue_product_name]


for product in quantity_by_product:
    quantity = quantity_by_product[product]

    if quantity > best_selling_product_quantity:
        best_selling_product_quantity = quantity
        best_selling_product_name = product


for product in revenue_by_product:
    revenue = revenue_by_product[product]
    if revenue > top_revenue_product_value:
        top_revenue_product_value = revenue
        top_revenue_product_name = product



print("List of products: ")
for product in quantity_by_product:
    if quantity_by_product[product] == 1:
        print(f"- {product} : {quantity_by_product[product]} piece")
    else:
        print(f"- {product} : {quantity_by_product[product]} pieces")
print()
print(f"Total revenue: {total_revenue} PLN")
print(f"Total quantity sold: {total_quantity_sold} pieces")
print(f"Average order value = {round(total_revenue/order_count,2)} PLN")

print(f"Best selling product overall: {best_selling_product_name} - {best_selling_product_quantity} pieces")
print(f"Product with highest revenue: {top_revenue_product_name} - {top_revenue_product_value} PLN ")
print()
print("List of revenue per category:")
for category in revenue_by_category:
    print(f"- {category} : {revenue_by_category[category]} PLN")


file.close()
