
from input_validations import product_validation, price_validation, quantity_validation

def update(inventory):

    if not inventory:
        print("INVENTORY IS EMPTY!")
        return

    what_product = product_validation()

    for product in inventory:

        if what_product == product["name"]:

            change_price = input("\nDo you want to change price (y/n)?: ")
            if change_price.lower() in ["y", "yes"]:
                new_price = price_validation()
                product["price"] = new_price
                print(f"PRODUCT UPDATE: {what_product} | New price: $ {new_price}")
            
            change_quantity = input("\nDo you want to change quantity (y/n)?: ")
            if change_quantity.lower() in ["y", "yes"]:
                new_quantity = quantity_validation()
                product["quantity"] = new_quantity
                print(f"PRODUCT UPDATE: {what_product} | New quantity: {new_quantity}")
                break

            if change_price.lower() not in ["y", "yes"] and change_quantity.lower() not in ["y", "yes"]:
                print("\nPRODUCT WAS NOT MODIFY!")
                break
                
    else:
        print("\nPRODUCT DOESN'T EXIST!")





    