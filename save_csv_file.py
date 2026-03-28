import csv
import os


def save_csv(inventory):
    """
    Saves the inventory data into a CSV file.

    Parameters:
        inventory (list): List of products (each product is a dictionary).

    Returns:
        None: Prints success or error messages.
    """

    # 1. Check if inventory is empty
    if not inventory:
        print("INVENTORY IS EMPTY! Nothing to save")
        return

    file_csv = "inventory-jp.csv"

    try:
        # 2. Open file in write mode (overwrite existing file)
        file = open(file_csv, "w", newline="")

        # Create CSV writer with correct column order
        writer = csv.DictWriter(file, fieldnames=["name", "price", "quantity"])

        # Write header row
        writer.writeheader()

        # Write all inventory data
        writer.writerows(inventory)

        # Close file manually
        file.close()

        # 3. Success message with full file path
        print(f"Inventory saved in: {os.path.abspath(file_csv)}")

    except PermissionError:
        print("ERROR: You don't have permission to modify this file.")

    except Exception as any_other_error:
        print(f"ERROR saving file: {any_other_error}")