
from interactive_menu import menu

# Initial inventory with sample products
inventory = [
    {"name": "Coffee", "price": float(4200), "quantity": 2},
    {"name": "Apple", "price": float(12500), "quantity": 1}
]

# Entry point of the program
if __name__ == "__main__":

    # Welcome message UI
    print()
    print("=" * 35)
    print(" WELCOME TO J-PRODUCT SUPERMARKET")
    print("=" * 35)

    # Start the interactive menu system
    end_message = menu(inventory)

    # Show final message when user exits
    print(end_message)