from add_product import new_product
from display_inventory import show_inventory
from search_product import search
from update_product import update
from delete_product import delete
from display_statistics import statistics

from save_csv_file import save_csv
from load_csv_file import load_csv


def menu(inventory):

    end_menu = 0

    while end_menu == 0:

        # Show menu options
        print("\n1. Add product")
        print("2. Display inventory")
        print("3. Search product")
        print("4. Update product")
        print("5. Delete product")
        print("6. Display statistics")
        print("7. Save CSV")
        print("8. Load CSV")
        print("9. Exit")

        # Get user option
        option = input("\nPlease select an option: ")
        print()

        # OPTION 1: Add product
        if option == "1":
            add_message = new_product(inventory)
            print(add_message)

        # OPTION 2: Show all products
        elif option == "2":
            show_inventory(inventory)

        # OPTION 3: Search product
        elif option == "3":

            # Check if inventory is empty
            if not inventory:
                print("INVENTORY IS EMPTY!")
            else:
                found = search(inventory)

                # If product not found
                if found == None:
                    print("\nPRODUCT DOESN'T EXIST!")
                else:
                    print("\nFOUND PRODUCT:")
                    print(f"Product: {found['name']} | Price: $ {found['price']} | Quantity: {found['quantity']}")

        # OPTION 4: Update product
        elif option == "4":
            update(inventory)

        # OPTION 5: Delete product
        elif option == "5":
            delete(inventory)

        # OPTION 6: Show statistics
        elif option == "6":

            # Check if inventory is empty before calculating stats
            if not inventory:
                print("\nINVENTORY IS EMPTY!")
            else:
                total_revenue, total_quantity, max_price, max_pricep, max_quantity, max_quantityp = statistics(inventory)

                print(f"Total revenue: $ {total_revenue:,}")
                print(f"Total product units: {total_quantity}")
                print(f"Most expensive product: {max_pricep} | Price: $ {max_price:,}")
                print(f"Highest stock product: {max_quantityp} | Quantity: {max_quantity}")

        # OPTION 7: Save data to CSV
        elif option == "7":
            save_csv(inventory)

        # OPTION 8: Load data from CSV
        elif option == "8":
            inventory = load_csv("inventory-jp.csv", inventory)

        # OPTION 9: Exit program
        elif option == "9":
            end_menu = 1

        # Invalid option
        else:
            print("PLEASE ENTER A VALID VALUE!")

    return "THANKS FOR USING OUR SERVICES!\n"