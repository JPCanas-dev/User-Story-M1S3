from input_validations import product_validation

def delete(inventory):

    if not inventory:
        print("INVENTORY IS EMPTY!")
        return

    what_product = product_validation()

    for product in inventory:
        if what_product == product["name"]:
            inventory.remove(product)
            print("\nPRODUCT DELETED SUCCESSFULLY!")
            break

    else:
        print("\nPRODUCT DOESN'T EXIST!")
