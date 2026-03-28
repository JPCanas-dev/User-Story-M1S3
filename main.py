
from interactive_menu import menu

# No docstrings are used here, because this file only acts as the program entry 
# point and contains no functions or classes.

# Initial inventory with sample products
inventory = [
    {"name": "Coffee", "price": float(4200), "quantity": 2},
    {"name": "Apple", "price": float(12500), "quantity": 1}
]

# Check if this file is running in this file (not imported)
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

# This program is a console-based Inventory Management System for a supermarket.
# It allows users to add, view, search, update, and delete products, as well as
# calculate basic statistics and save/load inventory data using CSV files.
# The system is modular and uses dictionaries and lists to manage product data efficiently.