import csv

def load_sales(filename):
    with open(filename) as file:
        reader = csv.DictReader(file)
        
        required_columns = ["order_id", "date", "product", "category", "quantity", "price"]
        missing_columns = []
        
        for column in required_columns:
            if column not in reader.fieldnames:
                missing_columns.append(column)
        if missing_columns:
            print(f"Error: missing required columns: {missing_columns}")
            exit()

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

def format_money(value):
    return f"{value:,.2f}".replace(",", " ")


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


    print("SALES-ANALYZER-CLI 1.0")
    print()
    print("Summary:")
    print(f"Total revenue : {format_money(total_revenue)} PLN")
    print(f"Total quantity sold : {total_quantity_sold} pieces")
    print(f"Average order value : {format_money(total_revenue / order_count)} PLN")
    print()
    print("Top results: ")
    print(f"Best-selling product overall: {top_selling_product_name} - {top_selling_product_quantity} pieces")
    print(f"Product with highest revenue: {top_revenue_product_name} - {format_money(top_revenue_product_value)} PLN")
    print(f"Category with highest revenue: {top_revenue_category_name} - {format_money(top_revenue_category_value)} PLN")
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
        print(f"- {category}: {format_money(revenue_by_category[category])} PLN")
    print()
    print("Revenue by product:")
    for product in revenue_by_product:
        print(f"- {product}: {format_money(revenue_by_product[product])} PLN")
    print()

    

def save_report(
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
    
    with open("sales_report.txt", "w") as file:
        file.write("SALES-ANALYZER-CLI 1.0 \n")
        file.write("\n")
        file.write("Summary:\n")
        file.write(f"Total revenue: {format_money(total_revenue)} PLN\n")
        file.write(f"Total quantity sold: {total_quantity_sold} pieces\n")
        file.write(f"Average order value: {format_money(total_revenue / order_count)} PLN\n") 
        file.write("\n")
        file.write("Top results: \n")
        file.write(f"Best-selling product overall: {top_selling_product_name} - {top_selling_product_quantity} pieces\n")
        file.write(f"Product with highest revenue: {top_revenue_product_name} - {format_money(top_revenue_product_value)} PLN\n")
        file.write(f"Category with highest revenue: {top_revenue_category_name} - {format_money(top_revenue_category_value)} PLN\n")
        file.write("\n")
        file.write("Products sold: \n")
        for product in quantity_by_product:
            if quantity_by_product[product] == 1:
                file.write(f"- {product}: {quantity_by_product[product]} piece\n")
            else:
                file.write(f"- {product}: {quantity_by_product[product]} pieces\n")
        file.write("\n")
        file.write("Revenue by category: \n")
        for category in revenue_by_category:
            file.write(f"- {category}: {format_money(revenue_by_category[category])} PLN\n")
        file.write("\n")
        file.write("Revenue by product:\n")
        for product in revenue_by_product:
            file.write(f"- {product}: {format_money(revenue_by_product[product])} PLN\n")


def main():
    try:
        sales = load_sales("sales.csv")
    except FileNotFoundError:
        print("Error: sales.csv file not found.")
        exit()
    except ValueError:
        print("Error: invalid numeric value in sales.csv.")
        exit()
    if not sales:
        print("Error: sales.csv contains no sales data.")
        exit()

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
    save_report(    
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


    print("Report saved to sales_report.txt")
    print()
    


if __name__ == "__main__":
    main()