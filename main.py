import json


with open("orders.json", 'r', encoding="utf-8") as file:
    orders = json.load(file)

print(orders)