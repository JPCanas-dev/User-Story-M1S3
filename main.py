from interactive_menu import menu

inventory = [
    {"name" : "Coffee", "price" : float(4200), "quantity" : 2},
    {"name" : "Apple", "price" : float(12500), "quantity" : 1}
]

if __name__ == "__main__":
    print()
    print("=" * 35)
    print(" WELCOME TO J-PRODUCT SUPERMARKET")
    print("=" * 35)
    end_message = menu(inventory)
    print(end_message)


