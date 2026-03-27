
def product_validation():

    correct_name = 0

    while correct_name == 0:

        name = input("Enter product name: ").strip()

        if not name:
            print("Empty name! Please enter a string\n")
        elif name.replace(" ", "").isalpha():
            correct_name = 1
        else:
            print("Please enter only letters!\n")

    return name

def price_validation():

    correct_price = 0

    while correct_price == 0:

        price = input("Enter price: ").strip()

        if not price:
            print("Empty price! Please enter a number\n")
        else:
            try:
                price = float(price)
                if price <= 0:
                    print("Price must be greater than 0!\n")
                else:
                    correct_price = 1
            except ValueError:
                print("Please enter only numbers!\n")

    return price

def quantity_validation():

    correct_quantity = 0

    while correct_quantity == 0:
            
        quantity = input("Enter quantity: ").strip()

        if not quantity:
            print("Empty quantity! Please enter a number\n")
        else:
            try:
                quantity = int(quantity)
                if quantity <= 0:
                    print("Quantity must be greater than 0!\n")
                else:
                    correct_quantity = 1
            except:
                print("Please enter only integers!\n")

    return quantity
