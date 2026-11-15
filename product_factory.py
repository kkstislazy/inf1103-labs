from product import Product, PhysicalProduct, DigitalProduct
from supplier import Supplier

class ProductFactory: 
    @staticmethod
    def create(product_type: str, product_id: str, name: str, price: float, stock: int, supplier: Supplier, extra: float) -> Product:
        if product_type == "physical":
            return PhysicalProduct(product_id, name, price, stock, supplier, extra)
        elif product_type == "digital":
            return DigitalProduct(product_id, name, price, stock, supplier, extra)
        else:
            raise ValueError("Invalid product type.")