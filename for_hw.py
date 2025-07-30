products = [
    "Banana",
    "Salt",
    "Bread",
    "Cheese",
    "Apple",
    "Orange",
    "Tomato",
    "Potato",
    "Carrot",
    "Milk",
    "Yogurt",
    "Butter",
    "Sugar",
    "Pepper",
    "Pasta",
    "Rice",
    "Beans",
    "Cereal",
    "Juice",
    "Coffee",
]

big_products = []
print(len(products))

for product in products:
    if product.endswith("d"):
        print(product)
    big_products.append(product.upper())
print(big_products)

some_product = "Nuddles"
if "a" in some_product.lower():
    products.append(some_product)
print(products)
list_with_replaced_a = []
for product in products:
    if len(product) > 5:
        print(product)
    list_with_replaced_a.append(product.replace("a", "*"))
print(list_with_replaced_a)
products.sort()
print(products)
