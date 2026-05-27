import csv

def load_sales(filename):
    with open(filename) as file:
        reader = csv.DictReader(file)
        sales = []

        for row in reader: 
            order_id = row["order_id"]
            date = row["date"]
            product = row["product"]
            category = row["category"]
            quantity = row["quantity"]
            price = row["price"]
    
            quantity = int(quantity)
            order_id = int(order_id)
            price = float(price)
    
    
            sale = {
                "order_id": order_id,
                "date": date,
                "product": product,
                "category": category,
                "quantity": quantity,
                "price": price,
           }
            sales.append(sale)

    
        return sales


def calculate_metrics(sales):

    total_revenue = 0
    total_quantity_sold = 0
    order_count = 0
    quantity_by_product = {}
    revenue_by_product = {}
    revenue_by_category = {}

    for sale in sales:

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

    return total_revenue, total_quantity_sold, order_count, quantity_by_product, revenue_by_product, revenue_by_category


def find_top_item(data):
    top_data_name = list(data.keys())[0]
    top_data_value = data[top_data_name]
    for item in data:
        if data[item] > top_data_value:
            top_data_value = data[item]
            top_data_name = item

    return top_data_name, top_data_value


def print_report(
    total_revenue,
    total_quantity_sold,
    order_count,
    top_selling_product_name,
    top_selling_product_quantity,
    top_revenue_product_name,
    top_revenue_product_value,
    top_revenue_category_name,
    top_revenue_category_value,
    quantity_by_product,
    revenue_by_category,
    revenue_by_product
    ):


    print("SALES ANALYZER REPORT")
    print()
    print("Summary:")
    print(f"Total revenue : {round(total_revenue, 2)} PLN")
    print(f"Total quantity sold : {total_quantity_sold} pieces")
    print(f"Average order value : {round(total_revenue / order_count, 2)}")
    print()
    print("Top results: ")
    print(f"Best-selling product overall: {top_selling_product_name} - {top_selling_product_quantity} pieces")
    print(f"Product with highest revenue: {top_revenue_product_name} - {round(top_revenue_product_value, 2)} PLN")
    print(f"Category with highest revenue: {top_revenue_category_name} - {round(top_revenue_category_value, 2)} PLN")
    print()
    print("Products sold: ")
    for product in quantity_by_product:
        if quantity_by_product[product] == 1:
            print(f"- {product}: {quantity_by_product[product]} piece")
        else:
            print(f"- {product}: {quantity_by_product[product]} pieces")
    print()
    print("Revenue by category: ")
    for category in revenue_by_category:
        print(f"- {category}: {round(revenue_by_category[category], 2)} PLN")
    print()
    print("Revenue by product:")
    for product in revenue_by_product:
        print(f"- {product}: {round(revenue_by_product[product], 2)} PLN")


def main():
    sales = load_sales("sales.csv")
    total_revenue, total_quantity_sold, order_count, quantity_by_product, revenue_by_product, revenue_by_category = calculate_metrics(sales)
    top_selling_product_name, top_selling_product_quantity = find_top_item(quantity_by_product)
    top_revenue_product_name, top_revenue_product_value = find_top_item(revenue_by_product)
    top_revenue_category_name, top_revenue_category_value = find_top_item(revenue_by_category)
    print_report( 
        total_revenue,
        total_quantity_sold,
        order_count,
        top_selling_product_name,
        top_selling_product_quantity,
        top_revenue_product_name,
        top_revenue_product_value,
        top_revenue_category_name,
        top_revenue_category_value,
        quantity_by_product,
        revenue_by_category,
        revenue_by_product
    )


if __name__ == "__main__":
    main()