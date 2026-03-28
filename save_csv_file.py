import csv
import os

def save_csv(inventory):
    
    # 1. Validar que el inventario no esté vacío
    if not inventory:
        print("INVENTORY IS EMPTY! Nothing to save")
        return

    file_csv = "inventory-jp.csv"

    try:
        # 2. Intentar guardar el archivo
        file = open(file_csv, "w", newline = "")

        writer = csv.DictWriter(file, fieldnames = ["name", "price", "quantity"])  # orden correcto
        writer.writeheader()
        writer.writerows(inventory)

        file.close()

        # 3. Mensaje de éxito con ruta
        print(f"Inventory saved in: {os.path.abspath(file_csv)}")

    except PermissionError:
        print("ERROR: You don't have permission to modify this file.")

    except Exception as any_other_error:
        print(f"ERROR saving file: {any_other_error}")