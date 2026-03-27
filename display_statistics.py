
def calculations(inventory):

    total_revenue = 0
    total_quantity = 0
    max_price = 0
    max_quantity = 0

    total_quantity += sum(product["quantity"] for product in inventory)
    subtotal = (lambda p: p["price"]*p["quantity"])
    total_revenue += sum(subtotal(product) for product in inventory)

    for product in inventory:
        if product["price"] > max_price:
            max_price = product["price"]
            max_pricep = product["name"]

    for product in inventory:
        if product["quantity"] > max_quantity:
            max_quantity = product["quantity"]
            max_quantityp = product["name"]

    return total_revenue, total_quantity, max_price, max_pricep, max_quantity, max_quantityp