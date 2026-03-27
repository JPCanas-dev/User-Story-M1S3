from input_validations import product_validation

def find_product(inventory):

    what_product = product_validation()

    for product in inventory:
        if what_product == product["name"]:
            return product
        
    return None
        
    



    