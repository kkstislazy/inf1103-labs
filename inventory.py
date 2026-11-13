from product import Product

class Inventory: 
    def __init__(self) -> None:
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> bool:
        product_id = product.get_product_id().lower()

        for p in self.__products: 
            if p.get_product_id().lower() == product_id:
                print("Error: Product ID already exists.")
                return False

        self.__products.append(product)
        return True

    def find_product(self, product_id: str) -> Product | None:
        for p in self.__products: 
            if p.get_product_id().lower() == product_id.lower():
                return p 
            
        return None

    def display_all(self) -> None:
        print("\nCurrent Inventory")

        if not self.__products:
            print("-" * 40)
            print("No products in inventory.")
            print("-" * 40)
        else: 
            for p in self.__products:
                p.display_information()

    def get_products(self) -> list[Product]:
        return self.__products

    def remove_product(self, product_id: str) -> None:
        product = self.find_product(product_id)

        if product: 
            self.__products.remove(product)
        else: 
            print("Could not find the product to be deleted.")

            
