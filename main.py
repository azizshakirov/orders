import json


with open("orders.json", 'r', encoding="utf-8") as file:
    orders = json.load(file)

customers = []
for order in orders:
    name = order.get('customer_name')
    items = order.get("items")
    total = sum([item['price']*item['quantity'] for item in items])
    customer = {'name' : name, "total" : total}
    customers.append(customer)

for customer in customers:
    print(f"{customer['name']} -> {customer['total']} USD" )
