import csv

def save_csv(inventory):
    with open("inventory-jp.csv", "w", newline = "") as file:
        writer = csv.DictWriter(file, fieldnames = ["name", "quantity", "price"])

        writer.writeheader()
        writer.writerows(inventory)

    print("INVENTORY SUCCESSFULLY SAVE!")