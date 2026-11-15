from discount_strategy import DiscountStrategy, NoDiscount, PercentageDiscount, BulkDiscount
from order import Order
from product import PhysicalProduct
from supplier import Supplier
from product_factory import ProductFactory
from input_helper import get_positive_float
from csv_reader import load_products
from inventory import Inventory


def run_lab9_tests() -> None:

    # 1 Strategy Pattern tests
    print("1. Discount Strategy test")
    print("-"*40)

    no_discount = NoDiscount()
    print(f'No discount: ${no_discount.apply(100):.2f}')

    percent = PercentageDiscount(10)
    print(f'Percentage discount: ${percent.apply(100):.2f}')
    bulk = BulkDiscount(200,20)
    print(f'Bulk discount: ${bulk.apply(250):.2f}')

    supplier = Supplier("S001", "NA", "na-sty@gmail.com")
    product = PhysicalProduct("PP001", "Baby Angel", 100.0, 20, supplier, 10)
    order = Order("001")
    order.add_order_line(product, 1)
    print(f'Total before discount: ${order.calculate_total():.2f}')
    order.set_discount(percent)
    print(f'Total after discount: ${order.calculate_total():.2f}')

    # 2 Factory Pattern tests
    print('-'*40)
    print("2. Product Factory Tests")
    print('-'*40)

    physical_product = ProductFactory.create('physical', 'PP002', 'POP', 200, 20, supplier, 10)
    digital_product = ProductFactory.create('digital', 'DP001', "iTunes", 9.90, 100000, supplier, 6.7)
    print("Products successfully created: ")
    print(type(physical_product).__name__)
    print(type(digital_product).__name__)

    try: 
        bad_product = ProductFactory.create('service', 'B001', 'NPY', 100, 20, supplier, 10)
    except ValueError as e: 
        print(f'{e}. Product could not be created.')

    #3 Validation tests
    print('-'*40)
    print("2. Product Factory Tests")
    print('-'*40)

    try: 
        bad_product2 = ProductFactory.create('physical', 'PP003', 'FAF', -20, 1, supplier, 0.1)
    except ValueError as e:
        print(f'{e}. Product could not be created.')

    try: 
        bad_product3 = ProductFactory.create('physical', 'PP003', 'FAF', 20, -1, supplier, 0.1)
    except ValueError as e:
        print(f'{e}. Product could not be created.')

    try:
        order.add_order_line(product, 0)
    except ValueError as e:
        print(e)

    #4 Exception Handling Tests
    print('-'*40)
    print("2. Exception Handling Tests")
    print('-'*40)

    value = get_positive_float("Enter a positive number: ")
    print(f"Accepted value: {value}")

    inventory = Inventory()

    load_products("products.csv", inventory, supplier)
    print("\nProducts currently in inventory.")
    inventory.display_all()


        
