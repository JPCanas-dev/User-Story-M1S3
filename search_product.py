def find_product(inventory):

    if not inventory:
        print("\nINVENTORY IS EMPTY!")

    what_product = input("Enter product name including mayus/minus letters: ")

    for product in inventory:
        if what_product == product["name"]:
            return product
            break

    return None
        
    



    