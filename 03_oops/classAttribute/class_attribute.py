class Product:
    def __init__(self,name, price) -> None:
        self.name = name
        self._price = price
        
    # @property
    # def price(self):
    #     return self._price

     
    # @price.setter
    # def price(self, value):
    #     if isinstance(value, (int, float)):
    #         raise ValueError("price is number")
    #     if value <0:
    #         raise value('''price can't be negative''')
        
    def get_price(self):
        return self._price

    def set_price(self, value):
        if isinstance(value, (int, float)):
            raise ValueError("price is number")
        if value <0:
            raise value('''price can't be negative''')
    
# create th instance of class 
product = Product("laptop", 12000)
print(product.get_price())
print(product.price())
