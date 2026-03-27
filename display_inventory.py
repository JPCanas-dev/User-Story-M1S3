
def show_inventory(inventory):

    for data in inventory:
        print(f"Product: {data['name']} | Price: $ {data['price']} | Quantity: {data['quantity']}")

