from order_line import OrderLine
from product import Product

class Order:
    def __init__(self, order_id: str) -> None:
        self.__order_id = order_id
        self.__order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)


    def calculate_total(self) -> float: 
        total: float = 0.0 
        for o in self.__order_lines:
            total += o.calculate_subtotal()

        return total

