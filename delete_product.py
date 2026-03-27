
def delete(inventory):

    what_product = input("Enter product name including mayus/minus: ")

    for product in inventory:
        if what_product == product["name"]:
            inventory.remove(product)
            print("\nPRODUCT SUCCESSFULLY DELETED!")
            break

    else:
        print("\nPRODUCT DOESN'T EXIST!")
