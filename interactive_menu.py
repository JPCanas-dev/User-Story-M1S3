from add_product import new_product
from display_inventory import show_inventory
from search_product import find_product

inventory = [
    {"name" : "Coffee", "price" : float(4200), "quantity" : 2},
    {"name" : "Apple", "price" : float(12500), "quantity" : 1}
]

def menu(inventory):

    end_menu = 0

    while end_menu == 0:

        print("\n1. Add product")
        print("2. Search product")
        print("3. Update product")
        print("4. Delete product")
        print("5. Display inventory")
        print("6. Display statistics")
        print("7. Save CSV")
        print("8. Load CSV")
        print("9. Exit")

        option = input("\nPlease select an option: ")
        print()

        if option == "1":
            success_add = new_product(inventory)
            print(success_add)

        elif option == "2":

            foundp = find_product(inventory)
            if foundp == None:
                print("\nPRODUCT DOESN'T EXIST!")
            else:
                print("\nFOUND PRODUCT:")
                print(f"Product: {foundp['name']} | Price: $ {foundp['price']} | Quantity: {foundp['quantity']}")

        elif option = "3":

        elif option == "5":
            show_inventory(inventory)

            
menu(inventory)





