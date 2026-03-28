
from input_validations import product_validation

def delete(inventory):
    """
    Deletes a product from the inventory list by name.

    Parameters:
        inventory (list): List of products (each product is a dictionary).

    Returns:
        None: Prints messages depending on the result.
    """

    # Check if inventory is empty
    if not inventory:
        print("INVENTORY IS EMPTY!")
        return

    # Get validated product name from user
    what_product = product_validation()

    # Search product in inventory
    for product in inventory:
        if what_product == product["name"]:
            # Remove product if found
            inventory.remove(product)
            print("\nPRODUCT DELETED SUCCESSFULLY!")
            break

    else:
        # Runs if product was not found in loop
        print("\nPRODUCT DOESN'T EXIST!")
