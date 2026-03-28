
from input_validations import product_validation, price_validation, quantity_validation

def update(inventory):
    """
    Updates the price and/or quantity of a product in the inventory.

    Parameters:
        inventory (list): List of products (each product is a dictionary).

    Returns:
        None: Prints messages depending on the update result.
    """

    # Check if inventory is empty
    if not inventory:
        print("INVENTORY IS EMPTY!")
        return

    # Get product name from user
    what_product = product_validation()

    # Search product in inventory
    for product in inventory:

        if what_product == product["name"]:

            # Ask if user wants to update price
            change_price = input("\nDo you want to change price (y/n)?: ")

            if change_price.lower() in ["y", "yes"]:
                new_price = price_validation()
                product["price"] = new_price
                print(f"PRODUCT UPDATE: {what_product} | New price: $ {new_price}")

            # Ask if user wants to update quantity
            change_quantity = input("\nDo you want to change quantity (y/n)?: ")

            if change_quantity.lower() in ["y", "yes"]:
                new_quantity = quantity_validation()
                product["quantity"] = new_quantity
                print(f"PRODUCT UPDATE: {what_product} | New quantity: {new_quantity}")

            # If no changes were made
            if change_price.lower() not in ["y", "yes"] and change_quantity.lower() not in ["y", "yes"]:
                print("\nPRODUCT WAS NOT MODIFY!")

            break

    # If product was not found
    else:
        print("\nPRODUCT DOESN'T EXIST!")





    