
def statistics(inventory):
    """
    Calculates basic statistics from the inventory.

    Parameters:
        inventory (list): List of products (each product is a dictionary).

    Returns:
        tuple: Total revenue, total quantity, most expensive product price and name,
               and product with highest quantity and its name.
    """

    # Initialize variables
    total_revenue = 0
    total_quantity = 0
    max_price = 0
    max_quantity = 0

    # lambda use: function to calculate revenue per product
    subtotal = (lambda p: p["price"] * p["quantity"])

    # Calculate total revenue
    total_revenue += sum(subtotal(product) for product in inventory)

    # Calculate total quantity of all products
    total_quantity += sum(product["quantity"] for product in inventory)

    # Find product with highest price
    for product in inventory:
        if product["price"] > max_price:
            max_price = product["price"]
            max_pricep = product["name"]

    # Find product with highest quantity
    for product in inventory:
        if product["quantity"] > max_quantity:
            max_quantity = product["quantity"]
            max_quantityp = product["name"]

    # Return all calculated values
    return total_revenue, total_quantity, max_price, max_pricep, max_quantity, max_quantityp