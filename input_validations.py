
def product_validation():
    """
    Validates that the product name is not empty and contains only letters.

    Returns:
        str: Valid product name entered by the user.
    """

    correct_name = 0

    while correct_name == 0:

        # Ask user for product name
        name = input("Enter product name: ").strip()

        # Check if input is empty
        if not name:
            print("Empty name! Please enter a string\n")

        # Check if input contains only letters and spaces
        elif name.replace(" ", "").isalpha():
            correct_name = 1

        else:
            print("Please enter only letters!\n")

    return name


def price_validation():
    """
    Validates that the price is a number greater than 0.

    Returns:
        float: Valid price entered by the user.
    """

    correct_price = 0

    while correct_price == 0:

        # Ask user for price
        price = input("Enter price: ").strip()

        # Check if input is empty
        if not price:
            print("Empty price! Please enter a number\n")

        else:
            try:
                price = float(price)

                # Check if price is valid (> 0)
                if price <= 0:
                    print("Price must be greater than 0!\n")
                else:
                    correct_price = 1

            except ValueError:
                print("Please enter only numbers!\n")

    return price


def quantity_validation():
    """
    Validates that the quantity is an integer greater than 0.

    Returns:
        int: Valid quantity entered by the user.
    """

    correct_quantity = 0

    while correct_quantity == 0:

        # Ask user for quantity
        quantity = input("Enter quantity: ").strip()

        # Check if input is empty
        if not quantity:
            print("Empty quantity! Please enter a number\n")

        else:
            try:
                quantity = int(quantity)

                # Check if quantity is valid (> 0)
                if quantity <= 0:
                    print("Quantity must be greater than 0!\n")
                else:
                    correct_quantity = 1

            except ValueError:
                print("Please enter only integers!\n")

    return quantity