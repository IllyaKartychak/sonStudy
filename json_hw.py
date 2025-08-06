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
cost_of_samsung_products = 0
products_with_good_discount_percentage = []
laptops_products = []

for product in products:
    cost_of_product = product["price"] * product["stock"]
    cost_of_products += cost_of_product
    if "discountPercentage" in product and product["discountPercentage"] > 15:
        products_with_good_discount_percentage.append(product)
    if "category" in product and product["category"] == "laptops":
        laptops_products.append(product)
    if "brand" in product:
        if product["brand"] == "Samsung":
            cost_of_samsung_products += cost_of_product
        if product["brand"] in group_by_brand:
            group_by_brand[product["brand"]].append(product)

# pprint(group_by_brand)
pprint(cost_of_products)
pprint(cost_of_samsung_products)
# pprint(products_with_good_discount_Percentage)
# pprint(laptops_products)
