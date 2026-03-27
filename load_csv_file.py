
import csv

def load_csv():
    inventory = []

    try:
        with open("inventory-jp.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                inventory.append({
                    "name": row["name"],
                    "price": float(row["price"]),
                    "quantity": int(row["quantity"])
                })

        print("INVENTORY SUCCESSFULLY LOADED!")
        return inventory

    except FileNotFoundError:
        print("FILE NOT FOUND!")
        return []