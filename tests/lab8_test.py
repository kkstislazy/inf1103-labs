from product import Product
from supplier import Supplier 
from inventory import Inventory
from order import Order

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