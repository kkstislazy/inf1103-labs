from product import Product

class OrderLine: 
    def __init__(self, product: Product, quantity: int) -> None:
        self.__product = product
        self.__quantity = quantity

    def calculate_subtotal(self) -> float:
        price = self.__product.get_price()
        subtotal: float = price * self.__quantity

        return subtotal
