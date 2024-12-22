import csv

class Item:
    pay_rate = 0.5 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # the received arguments 
        assert price>=0, f"price {price} is not greater than or equal to zero!"
        assert quantity>=0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to the Object
        self._name= name
        self.price = price
        self.quantity = quantity

        # Action to execute

        Item.all.append(self)
    
    @property
    # Property Decorator = Read-only Attribute
    def name(self):
        return self._name
    
    @name.setter

    def name(self, value):
        if(len(value)> 10):
            raise Exception(" The name is too long !")
        else:
            self.__name = value
    def total_price(self):
        return self.price * self.quantity
    
    def discount(self):
        self.price = self.price * self.pay_rate
    
    @classmethod

    def instant_from_csv(cls):
        with open('D:/Project/Python_Tutorial/03_oops/class vs static method.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )
    @staticmethod

    def is_integer(num):

        if(isinstance(num, float)):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"