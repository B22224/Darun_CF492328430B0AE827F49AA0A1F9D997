def linear_search_product(products, target_product):
    indices = []
    for i, product in enumerate(products):
        if product == target_product:
            indices.append(i)
    return indices

products = ["Apple", "Banana", "Apple", "Orange", "Apple"]
target_product = "Apple"

result = linear_search_product(products, target_product)
if result:
    print(f"The target product '{target_product}' was found at indices: {result}")
else:
    print(f"The target product '{target_product}' was not found.")