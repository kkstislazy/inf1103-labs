from abc import ABC, abstractmethod
from can_be_shipped import CanBeShipped
from supplier import Supplier

class Product(ABC): 
    def __init__(self, product_id:str, name:str, price: float, stock: int, supplier: Supplier) -> None:
        self.__product_id = product_id
        self.__name = name

        if price <= 0:
            raise ValueError("Price has to be greater than 0.")
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number.")
        self.__price = price

        if stock < 0: 
            raise ValueError("Stock has to be greater than 0.")
        if not isinstance(stock, int):
            raise TypeError("Stock must be a whole number.")
        self.__stock = stock
        
        self.__supplier: Supplier = supplier

    def display_current_stock(self) -> None:
        print(f'Product Name: {self.__name}')
        print(f'Current stock: {self.__stock}')

    def update_stock(self, quantity: int) -> None:
        self.__stock = quantity

    def display_information(self, extra_info: str | None = None) -> None:
        print("-" * 40)
        print(f'ID: {self.__product_id}')
        print(f'Name: {self.__name}')
        print(f'Price: ${self.__price:.2f}')
        print(f'Stock: {self.__stock}')

        if extra_info: 
            print(extra_info)

        print("-" * 40)

    def get_product_id(self) -> str:
        return self.__product_id

    def to_dict(self) -> dict:
        product_dict = {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "supplier": self.__supplier.to_dict()
        }

        return product_dict

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass

    def display_supplier_information(self) -> None:
        self.__supplier.display_information()

    def get_price(self) -> float:
        return self.__price

class PhysicalProduct(Product, CanBeShipped): 
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, weight: float) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight = weight

    def display_information(self) -> None:
        super().display_information(f'Weight: {self.__weight}kg')

    def get_fulfilment_info(self) -> str:
        return "This product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        shipping_cost = self.__weight * 5
        return shipping_cost

    def to_dict(self) -> dict:
        product_dict = super().to_dict()

        product_dict["type"] = "physical"
        product_dict["weight"] = self.__weight

        return product_dict

        
class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, download_size: float) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size = download_size

    def display_information(self) -> None:
        super().display_information(f'Download size: {self.__download_size}MB')

    def get_fulfilment_info(self) -> str:
        return "This product is delivered digitally."

    def to_dict(self) -> dict:
        product_dict = super().to_dict()

        product_dict["type"] = "digital"
        product_dict["download_size"] = self.__download_size

        return product_dict
