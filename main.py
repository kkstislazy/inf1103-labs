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