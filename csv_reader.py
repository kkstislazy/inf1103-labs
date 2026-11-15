from inventory import Inventory
from supplier import Supplier
from product_factory import ProductFactory

import csv

def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    try: 
        file = open(path, newline="")
    except FileNotFoundError:
        print(f'Products file not found: {path}') 
    else: 
        with file: 
            reader = csv.reader(file)
            next(reader)
            counter = 0
            for row in reader: 

                try: 
                    product = ProductFactory.create(row[0], row[1], row[2], float(row[3]), int(row[4]), supplier, 0.0) # used 0.0 for extra info (weight/download_size) since the csv does not contain that data
                except ValueError:
                    print("Invalid value detected. Skipping product.") 
                    continue

                if inventory.add_product(product):
                    counter += 1

            print(f'{counter} products loaded.')
            
    finally: 
        print("Load attempt finished")