import requests
from pprint import pprint


url = "https://dummyjson.com/products"
params = {"limit": 1000, "skip": 0}

response = requests.get(url, params=params)

response_json = response.json()
products = response_json["products"]

group_by_brand = {
    "Apple": [],
    "Samsung": [],
}

cost_of_products = 0
cost_of_Samsung_products = 0
products_with_good_discount_Percentage = []
laptops_products = []

for product in products:

    cost_of_products += product["price"] * product["stock"]
    if "discountPercentage" in product and product["discountPercentage"] > 15:
        products_with_good_discount_Percentage.append(product)
    if "category" in product and product["category"] == "laptops":
        laptops_products.append(product)
    if "brand" in product and product["brand"] == "Samsung":
        cost_of_Samsung_products += product["price"] * product["stock"]
    if "brand" in product and product["brand"] in group_by_brand:
        group_by_brand[product["brand"]].append(product)
# pprint(group_by_brand)
pprint(cost_of_products)
pprint(cost_of_Samsung_products)
# pprint(products_with_good_discount_Percentage)
# pprint(laptops_products)
