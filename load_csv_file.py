import csv

def load_csv(path, current_inventory):
    loaded_inventory = []
    invalid_rows = 0

    try:
        # I used open() and close() in save, let's use with open() here in load 
        with open(path, "r", encoding="utf-8") as file:
            csv_rows = csv.reader(file)

            # 1. Validar encabezado
            header = next(csv_rows, None)
            if header != ["name", "price", "quantity"]:
                print("INVALID HEADER! Must be: name, price, quantity")
                return current_inventory

            # 2. Leer filas
            for current_row in csv_rows:

                # Validar número de columnas
                if len(current_row) != 3:
                    invalid_rows += 1
                    continue

                # desempaquetado (unpacking): estoy extrayendo valores, no asignándolos 
                name, price, quantity = current_row

                try:
                    price = float(price)
                    quantity = int(quantity)

                    # Validar valores mayores a 0
                    if price <= 0 or quantity <= 0:
                        invalid_rows += 1
                        continue

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

    # 3. Preguntar acción al usuario
    choice = input("\nOverwrite current inventory (y/n)?: ").strip()

    if choice.lower in ["yes", "y"]:
        final_inventory = loaded_inventory
        action = "REPLACE CURRENT INVENTORY"

    else:
        # 4. Fusión de inventarios
        # creo copia para no modificar el inventario original. Sin el .copy 
        # cualquier cambio en final_inventory afecta el original inmediatamente
        final_inventory = current_inventory.copy()

        for new_product in loaded_inventory:
            found = False

            for product in final_inventory:
                if product["name"] == new_product["name"]:
                    # Política: sumar cantidad y actualizar precio
                    product["quantity"] += new_product["quantity"]
                    product["price"] = new_product["price"]
                    found = True
                    break

            if not found:
                final_inventory.append(new_product)

        action = "MERGE CURRENT INVENTORY"

    # 5. Resumen final
    print("\n============== SUMMARY ==============")
    print(f"Products loaded: {len(loaded_inventory)}")
    print(f"Invalid rows skipped: {invalid_rows}")
    print(f"Action: {action}")

    return final_inventory