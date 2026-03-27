
from input_validations import product_validation, price_validation, quantity_validation

def new_product (inventory):

    name = product_validation()
    price = price_validation()
    quantity = quantity_validation()

    # name = input("Enter product name: ")
    # price = float(input("Enter price: "))
    # quantity = int(input("Enter quantity: "))

    product_added = {
        "name" : name,
        "price" : price,
        "quantity" : quantity
    }

    inventory.append(product_added)

    return"\nPRODUCT SUCCESSFULLY ADDED!"



