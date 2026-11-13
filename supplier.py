class Supplier:
    def __init__(self, supplier_id: str, name: str, email: str):
        self.__supplier_id = supplier_id
        self.__supplier_name = name 
        self.__supplier_email = email

    def display_information(self):
        print("Supplier Information")
        print("-"*40)
        print(f'Supplier ID: {self.__supplier_id}')
        print(f'Supplier Name: {self.__supplier_name}')
        print(f'Supplier Email: {self.__supplier_email}')

    