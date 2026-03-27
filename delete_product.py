from input_validations import product_validation

def delete(inventory):

    what_product = product_validation()

    for product in inventory:
        if what_product == product["name"]:
            inventory.remove(product)
            print("\nPRODUCT SUCCESSFULLY DELETED!")
            break

    else:
        print("\nPRODUCT DOESN'T EXIST!")
