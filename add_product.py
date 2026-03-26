
def new_product (inventory):

    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    product_added = {
        "name" : name,
        "price" : price,
        "quantity" : quantity
    }

    inventory.append(product_added)

    return"\nPRODUCT ADDED!"



