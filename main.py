import json
import os

from product import Product
from inventory import Inventory

FILE_NAME = "inventory.json"

def load_inventory():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                inventory = Inventory()
                load = json.load(file)

                for p in load:
                    product = Product(p["id"], p["name"], p["price"], p["stock"])
                    inventory.add_product(product)

                print("inventory.json file found.")
                print("Inventory loaded successfully.")
                return inventory
        except (json.JSONDecodeError, OSError):
            print("Error loading inventory. Starting with empty inventory.")
            return Inventory()
    else:
        print("inventory.json not found.")
        print("Starting with empty inventory.")
        return Inventory()

def save_inventory(inventory):
    product_list = []

    for p in inventory.get_products():
        product = p.to_dict()
        product_list.append(product)

    with open(FILE_NAME, "w") as file:
        json.dump(product_list, file, indent=4)

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

def add_product(inventory):
    print("\nAdd New Product")
    product_id = input("\nProduct ID: ").strip()
    if not product_id: 
        print("Error: Product ID cannot be empty.")
        return 
                
    product_name = input("\nProduct Name: ").strip()
    if not product_name:
        print("Error: Product name cannot be empty.")
        return
    
    try: 
        product_price = float(input("\nPrice: "))
        product_stock = int(input("\nStock quantity: "))
    
        if product_price < 0 or product_stock < 0:
            print("Error: Price and stock cannot be negative.")
            return
    except ValueError:
        print("Error: Please enter a valid price and stock quantity.")
        return
    
    product = Product(product_id, product_name, product_price, product_stock)

    if inventory.add_product(product):
        print("Product added successfully.")


def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("\nEnter Product ID: ").strip().lower()
    product = inventory.search_product(product_id)

    if product:
        print("Product found:")
        product.display_current_stock()

        try: 
            new_stock = int(input("New stock quantity: "))

            if new_stock < 0:
                print("Error: Stock cannot be negative.")
                return
        except ValueError: 
            print("Error: Please enter a valid integer.")
            return

        product.update_stock(new_stock)
        print("Stock updated successfully.")
        return

    else: 
        print("Product not found.")

def search_product(inventory):
    print("\nSearch Product")
    product_id = input("Enter product ID: ").strip().lower()
    product = inventory.search_product(product_id)

    if product:
        product.display_information()
    else: 
        print("Product not found.")

def main():
    inventory = load_inventory()

    while True:
        display_menu()
        option = input("\nEnter option: ").strip()

        if option == "1":
            inventory.display_all()

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
                print(f'Inventory saved successfully to {FILE_NAME}.')
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

            print("Thank you for using the Inventory Management System!")
            print("Program terminated.")

            break

        else: 
            print("Invalid option. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()       