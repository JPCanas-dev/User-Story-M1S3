
from input_validations import product_validation, price_validation, quantity_validation

def new_product(inventory):
    """
    Adds a new product to the inventory list.

    Parameters:
        inventory (list): List of products (each product is a dictionary).

    Returns:
        str: Success message after adding the product.
    """

    # Get validated product name from user
    name = product_validation()

    # Get validated product price from user
    price = price_validation()

    # Get validated product quantity from user
    quantity = quantity_validation()

    # Create product dictionary
    product_added = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    # Add product to inventory list
    inventory.append(product_added)

    # Return confirmation message
    return "\nPRODUCT ADDED SUCCESSFULLY!"



