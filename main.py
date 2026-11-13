import json
import os

from product import Product, PhysicalProduct, DigitalProduct
from inventory import Inventory
from supplier import Supplier
from order import Order

FILE_NAME = "inventory.json"

def load_inventory():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                inventory = Inventory()
                load = json.load(file)

                for p in load:
                    supplier = Supplier("S000", "Default Supplier", "test@email.com")
                    if p["type"] == "physical":
                        product = PhysicalProduct(p["id"], p["name"], p["price"], p["stock"], p["weight"])
                    elif p["type"] == "digital":
                        product = DigitalProduct(p["id"], p["name"], p["price"], p["stock"], p["download_size"])
                    else:
                        print(f'Unknown product type: {p["type"]}. Skipping product.')
                        continue
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
    
        if product_price < 0:
            print("Error: Price  cannot be negative.")
            return
        
        product_stock = int(input("\nStock quantity: "))

        if product_stock < 0:
            print("Error: Stock cannot be negative.")
            return

    except ValueError:
        print("Error: Please enter a valid price and stock quantity.")
        return

    print("\nSupplier Information")

    supplier_id = input("Supplier ID: ").strip()
    supplier_name = input("Supplier Name: ").strip()
    supplier_email = input("Supplier Email: ").strip()

    if not supplier_id or not supplier_name or not supplier_email: 
        print("Error: Supplier information cannot be empty.")
        return

    supplier = Supplier(supplier_id, supplier_name, supplier_email)

    product_type = input("\nProduct type: ").strip().lower()
    if product_type == "physical": 
        try: 
            product_weight = float(input("\nProduct weight (kg): "))

            if product_weight < 0:
                print("Product weight cannot be negative")
                return

        except ValueError: 
            print("Error: Please enter a valid weight.")
            return

        product = PhysicalProduct(product_id, product_name, product_price, product_stock, product_weight)
    
    elif product_type == "digital":
        try: 
            product_download_size = float(input("\nProduct download size (MB): "))

            if product_download_size < 0: 
                print("Product download size cannot be negative.")
                return

        except ValueError: 
            print("Error: Please enter a valid download size.")
            return
        
        product = DigitalProduct(product_id, product_name, product_price, product_stock, product_download_size)
    
    else: 
        print("Error: Please enter a valid product type 'physical' or 'digital'.")
        return
    
    if inventory.add_product(product):
        print("Product added successfully.")


def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("\nEnter Product ID: ").strip().lower()
    product = inventory.find_product(product_id)

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

def find_product(inventory):
    print("\nSearch Product")
    product_id = input("Enter product ID: ").strip().lower()
    product = inventory.find_product(product_id)

    if product:
        product.display_information()
    else: 
        print("Product not found.")

def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


def demonstrate_polymorphism(products: list[Product]) -> None:
    print("\nPOLYMORPHISM TEST")
    print("=" * 40)

    for product in products:
        product.display_information()
        print(product.get_fulfilment_info())


def run_lab_tests() -> None:
    print("\nLAB 8 RELATIONSHIP AND LSP TESTS")

    # 1. Association: Supplier and Product
    supplier = Supplier("S001", "ABC Supplier", "abc@email.com")

    physical_product = PhysicalProduct(
        "P001", "Keyboard", 50.0, 10, supplier, 0.5
    )

    print("\nASSOCIATION TEST")
    physical_product.display_supplier_information()

    # 2. Supplier and Product can exist independently
    del supplier
    physical_product.display_supplier_information()

    # 3. Aggregation: Inventory and Product
    inventory1 = Inventory()
    inventory2 = Inventory()

    inventory1.add_product(physical_product)

    print("\nAGGREGATION TEST")
    inventory1.remove_product("P001")
    inventory2.add_product(physical_product)

    print("Product transferred to second inventory:")
    inventory2.display_all()

    # 4. Create a digital product
    digital_supplier = Supplier(
        "S002", "XYZ Supplier", "xyz@email.com"
    )

    digital_product = DigitalProduct(
        "P002", "Software", 100.0, 20, digital_supplier, 500.0
    )

    # 5. Composition: Order creates its own OrderLines
    order1 = Order("O001")
    order2 = Order("O002")

    order1.add_order_line(physical_product, 2)
    order1.add_order_line(digital_product, 1)

    # Same Product can be referenced by another Order
    order2.add_order_line(physical_product, 1)

    print("\nCOMPOSITION TEST")
    print(f"Order 1 total: ${order1.calculate_total():.2f}")
    print(f"Order 2 total: ${order2.calculate_total():.2f}")

    # 6. LSP: Both subclasses accepted as Product
    print("\nLSP TEST")
    show_product_details(physical_product)
    show_product_details(digital_product)

    # 7. Polymorphism: Both subclasses in one Product collection
    demonstrate_polymorphism([
        physical_product,
        digital_product
    ])

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
            find_product(inventory)

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
    # main()       
    run_lab_tests()