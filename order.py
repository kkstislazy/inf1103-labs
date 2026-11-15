from order_line import OrderLine
from product import Product
from discount_strategy import DiscountStrategy, NoDiscount

class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy = None) -> None:
        self.__order_id = order_id
        self.__order_lines: list[OrderLine] = []
        self.__discount: DiscountStrategy = discount if discount is not None else NoDiscount()

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def set_discount(self, discount: DiscountStrategy) -> None: 
        self.__discount = discount


    def calculate_total(self) -> float: 
        total: float = 0.0 
        for o in self.__order_lines:
            total += o.calculate_subtotal()

        return self.__discount.apply(total)

