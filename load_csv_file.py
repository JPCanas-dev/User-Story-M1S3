import csv

# Path represents the file path or the file name
def load_csv(path, current_inventory):
    """
    Loads product data from a CSV file and validates it before merging or replacing inventory.

    Parameters:
        path (str): Path of the CSV file.
        current_inventory (list): Existing inventory list.

    Returns:
        list: Updated inventory after loading CSV data.
    """

    loaded_inventory = []
    invalid_rows = 0

    try:
        # Open file in read mode with UTF-8 encoding
        with open(path, "r", encoding="utf-8") as file:
            csv_rows = csv.reader(file)

            # 1. Validate header
            header = next(csv_rows, None)
            if header != ["name", "price", "quantity"]:
                print("INVALID HEADER! Must be: name, price, quantity")
                return current_inventory

            # 2. Read each row in CSV
            for current_row in csv_rows:

                # Validate number of columns
                if len(current_row) != 3:
                    invalid_rows += 1
                    continue

                # Unpacking values from row
                name, price, quantity = current_row

                try:
                    price = float(price)
                    quantity = int(quantity)

                    # Validate positive values
                    if price <= 0 or quantity <= 0:
                        invalid_rows += 1
                        continue

                    # Add valid product to temporary list
                    loaded_inventory.append({
                        "name": name,
                        "price": price,
                        "quantity": quantity
                    })

                except ValueError:
                    invalid_rows += 1
                    continue

        print("CSV LOADED SUCCESSFULLY!")

    except FileNotFoundError:
        print("ERROR: File not found!")
        return current_inventory

    except UnicodeDecodeError:
        print("ERROR: File encoding not supported!")
        print("Possible solutions:")
        print("- Save the file as UTF-8 encoding.")
        print("- If using Excel, export/save as 'CSV UTF-8'.")
        print("- Make sure the file was not saved in ANSI/Windows encoding.")
        return current_inventory

    except Exception as any_other_error:
        print(f"ERROR: {any_other_error}")
        return current_inventory

    # 3. Ask user what to do with loaded data
    choice = input("\nOverwrite current inventory (y/n)?: ").strip()

    # IMPORTANT FIX: correct usage of .lower()
    if choice.lower() in ["yes", "y"]:
        # Replace entire inventory
        final_inventory = loaded_inventory
        action = "REPLACE CURRENT INVENTORY"

    else:
        # 4. Merge inventories instead of replacing

        # Copy current inventory to avoid modifying original directly
        final_inventory = current_inventory.copy()

        for new_product in loaded_inventory:
            found = False

            for product in final_inventory:
                if product["name"] == new_product["name"]:
                    # If product exists: update quantity and price
                    product["quantity"] += new_product["quantity"]
                    product["price"] = new_product["price"]
                    found = True
                    break

            # If product does not exist, add it
            if not found:
                final_inventory.append(new_product)

        action = "MERGE CURRENT INVENTORY"

    # 5. Final summary report
    print("\n============== SUMMARY ==============")
    print(f"Products loaded: {len(loaded_inventory)}")
    print(f"Invalid rows skipped: {invalid_rows}")
    print(f"Action: {action}")

    return final_inventory