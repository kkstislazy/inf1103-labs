class Product: 
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def display_current_stock(self):
        print(f'Product Name: {self.__name}')
        print(f'Current stock: {self.__stock}')

    def update_stock(self, quantity):
        self.__stock = quantity

    def display_information(self):
        print("-" * 40)
        print(f'ID: {self.__product_id}')
        print(f'Name: {self.__name}')
        print(f'Price: ${self.__price:.2f}')
        print(f'Stock: {self.__stock}')
        print("-" * 40)

    def get_product_id(self):
        return self.__product_id

    def to_dict(self):
        product_dict = {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }

        return product_dict

