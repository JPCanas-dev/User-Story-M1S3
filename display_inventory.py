
def show_inventory(inventory):
    """
    Displays all products in the inventory list.

    Parameters:
        inventory (list): List of products (each product is a dictionary).

    Returns:
        None: Prints each product in a formatted way.
    """

    # Check if inventory is empty
    if not inventory:
        print("INVENTORY IS EMPTY!")
        return

    # Loop through all products and display them
    for product in inventory:
        print(f"Product: {product['name']} | Price: $ {product['price']} | Quantity: {product['quantity']}")

