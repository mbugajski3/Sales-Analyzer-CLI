
def load_sales(filename):
    file = open(filename)
    headers = next(file)
    sales = []

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
        order_id = int(order_id)
        price = float(price)
    
    
        sale = {
            "order_id" : order_id,
            "date" : date,
            "product" : product,
            "category" : category,
            "quantity" : quantity,
            "price" : price,
       }
        sales.append(sale)

    file.close()
    return sales

total_revenue = 0
total_quantity_sold = 0
order_count = 0
quantity_by_product = {}
revenue_by_product = {}
revenue_by_category = {}

sales = load_sales("sales.csv")

for sale in sales:

    order_id = sale["order_id"]
    date = sale["date"]
    product = sale["product"]
    category = sale["category"]
    quantity = sale["quantity"]
    price = sale["price"]
    
    
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

top_selling_product_name = list(quantity_by_product.keys())[0]
top_selling_product_quantity = quantity_by_product[top_selling_product_name]

top_revenue_product_name = list(revenue_by_product.keys())[0]
top_revenue_product_value = revenue_by_product[top_revenue_product_name]

top_revenue_category_name = list(revenue_by_category.keys())[0]
top_revenue_category_value = revenue_by_category[top_revenue_category_name]


for product in quantity_by_product:
    if quantity_by_product[product] > top_selling_product_quantity:
        top_selling_product_name = product
        top_selling_product_quantity = quantity_by_product[product]

for product in revenue_by_product:
    if revenue_by_product[product] > top_revenue_product_value:
        top_revenue_product_value = revenue_by_product[product]
        top_revenue_product_name = product

for category in revenue_by_category:
    if revenue_by_category[category] > top_revenue_category_value:
        top_revenue_category_value = revenue_by_category[category]
        top_revenue_category_name = category


print(f"Total revenue : {round(total_revenue,2)} PLN")
print(f"Total quantity sold : {total_quantity_sold} pieces")
print(f"Average order value : {round(total_revenue / order_count,2)}")
print(f"Best-selling product overall: {top_selling_product_name} - {top_selling_product_quantity} pieces")
print(f"Product with highest revenue: {top_revenue_product_name} - {round(top_revenue_product_value,2)} PLN")
print(f"Category with highest revenue: {top_revenue_category_name} - {round(top_revenue_category_value,2)} PLN")
