
def show_inventory(inventory):

    # if not inventory:
    #     print("INVENTORY IS EMPTY!")

    for data in inventory:
        print(f"Product: {data['name']} | Price: $ {data['price']} | Quantity: {data['quantity']}")

