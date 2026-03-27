
from input_validations import product_validation, price_validation, quantity_validation

def update(inventory):

    what_product = input("Enter product name including mayus/minus: ")

    for product in inventory:

        if what_product == product["name"]:

            change_price = input("\nDo you want to change price (y/n): ")
            if change_price in ["y", "Y", "yes", "YES"]:
                # new_price = float(input("Please enter new price: "))
                new_price = price_validation()
                product["price"] = new_price
            
            change_quantity = input("\nDo you want to change quantity (y/n): ")
            if change_quantity in ["y", "Y", "yes", "YES"]:
                new_quantity = int(input("Please enter new quantity: "))
                product["quantity"] = new_quantity
                break

    else:
        print("PRODUCT DOESN'T EXIST!")





    