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

        print("\n1. Add product")
        print("2. Display inventory")
        print("3. Search product")
        print("4. Update product")
        print("5. Delete product")
        print("6. Display statistics")
        print("7. Save CSV")
        print("8. Load CSV")
        print("9. Exit")

        option = input("\nPlease select an option: ")
        print()

        if option == "1":
            add_message = new_product(inventory)
            print(add_message)

        elif option == "2":
            show_inventory(inventory)

        elif option == "3":
            
            if not inventory:
                print("INVENTORY IS EMPTY!")
            else:
                found = search(inventory)
                if found == None:
                    print("\nPRODUCT DOESN'T EXIST!")
                else:
                    print("\nFOUND PRODUCT:")
                    print(f"Product: {found['name']} | Price: $ {found['price']} | Quantity: {found['quantity']}")

        elif option == "4":
            update(inventory)

        elif option == "5":
            delete(inventory)
        
        elif option == "6":
            
            if not inventory:
                print("\nINVENTORY IS EMPTY!")
            else:
                total_revenue, total_quantity, max_price, max_pricep, max_quantity, max_quantityp = statistics(inventory)
                print(f"Total revenue: $ {total_revenue:,}")
                print(f"Total product units: {total_quantity}")
                print(f"Most expensive product: {max_pricep} | Price: $ {max_price:,}")
                print(f"Highest stock product: {max_quantityp} | Quantity: {max_quantity}")

        elif option == "7":
            save_csv(inventory)

        elif option == "8":
            inventory = load_csv("inventory-jp.csv", inventory)
        
        elif option == "9":
            end_menu = 1

        else:
            print("PLEASE ENTER A VALID VALUE!")

    return"THANKS FOR USING OUR SERVICES!\n"