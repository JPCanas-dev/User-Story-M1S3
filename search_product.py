
from input_validations import product_validation

def search(inventory):
    """
    Searches for a product in the inventory by its name.

    Parameters:
        inventory (list): List of products (each product is a dictionary).

    Returns:
        dict or None: The product if found, otherwise None.
    """

    # Get validated product name from user
    what_product = product_validation()

    # Loop through all products in inventory
    for product in inventory:
        if what_product == product["name"]:
            # Return product if it matches
            return product

    # Return None if product is not found
    return None