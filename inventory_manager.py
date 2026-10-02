
import json
import os

FILE_NAME = "inventory.json"


def load_inventory():
    """Load inventory from JSON, or start with an empty list."""
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                inventory = json.load(file)
            print("inventory.json found.")
            print("Inventory loaded successfully.")
            return inventory
        except (json.JSONDecodeError, OSError):
            print("Error loading inventory. Starting with empty inventory.")
            return []
    else:
        print("inventory.json not found.")
        print("Starting with empty inventory.")
        return []


def save_inventory(inventory):
    """Save inventory to JSON."""
    with open(FILE_NAME, "w") as file:
        json.dump(inventory, file, indent=4)


def display_all(inventory):
    """Display all products."""
    print("\nCurrent Inventory")
    print("-" * 48)

    if not inventory:
        print("No products in inventory.")
    else:
        for product in inventory:
            print(
                f'ID: {product["id"]} | '
                f'Name: {product["name"]} | '
                f'Price: ${product["price"]:.2f} | '
                f'Stock: {product["stock"]}'
            )

    print("-" * 48)


def add_product(inventory):
    """Add a new product."""
    print("\nAdd New Product")

    product_id = input("Product ID: ").strip()

    if not product_id:
        print("Error: Product ID cannot be empty.")
        return

    if any(p["id"].lower() == product_id.lower() for p in inventory):
        print("Error: Product ID already exists.")
        return

    product_name = input("Product Name: ").strip()

    if not product_name:
        print("Error: Product name cannot be empty.")
        return

    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))

        if price < 0 or stock < 0:
            print("Error: Price and stock cannot be negative.")
            return

    except ValueError:
        print("Error: Please enter a valid price and stock quantity.")
        return

    inventory.append({
        "id": product_id,
        "name": product_name,
        "price": price,
        "stock": stock
    })

    print("Product added successfully!")


def update_stock(inventory):
    """Update the stock quantity of a product."""
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ").strip()

    for product in inventory:
        if product["id"].lower() == product_id.lower():
            print("Product Found:")
            print(f'Name: {product["name"]}')
            print(f'Current Stock: {product["stock"]}')

            try:
                new_stock = int(input("New Stock Quantity: "))

                if new_stock < 0:
                    print("Error: Stock cannot be negative.")
                    return

            except ValueError:
                print("Error: Please enter a valid integer.")
                return

            product["stock"] = new_stock
            print("Stock updated successfully!")
            return

    print("Product not found.")


def search_product(inventory):
    """Search for a product using its ID."""
    print("\nSearch Product")
    product_id = input("Enter Product ID: ").strip()

    for product in inventory:
        if product["id"].lower() == product_id.lower():
            print("Product Found")
            print("-" * 48)
            print(f'ID: {product["id"]}')
            print(f'Name: {product["name"]}')
            print(f'Price: ${product["price"]:.2f}')
            print(f'Stock: {product["stock"]}')
            print("-" * 48)
            return

    print("Product not found.")


def display_menu():
    print("\n" + "=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


def main():
    inventory = load_inventory()

    while True:
        display_menu()
        option = input("\nEnter option: ").strip()

        if option == "1":
            display_all(inventory)

        elif option == "2":
            add_product(inventory)

        elif option == "3":
            update_stock(inventory)

        elif option == "4":
            search_product(inventory)

        elif option == "5":
            print("Saving inventory...")
            try:
                save_inventory(inventory)
                print("Inventory saved successfully to inventory.json.")
            except OSError:
                print("Error: Unable to save inventory.")

        elif option == "6":
            print("Saving inventory before exit...")
            try:
                save_inventory(inventory)
                print("Inventory saved successfully.")
            except OSError:
                print("Error: Unable to save inventory.")
                print("Please check your file permissions.")
                continue

            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break

        else:
            print("Invalid option. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()