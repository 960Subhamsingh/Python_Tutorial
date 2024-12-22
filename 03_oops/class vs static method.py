class Item:
    pay_rate = 0.5 # The pay rate after 20% discount
    all=[]
    def __init__(self, name: str, price: float, quantity=0) -> None:
        # the recieved valid argument
        assert price >= 0, f"price{price} is not greater than or equal to zero!"
        assert quantity>=0, f"Quantity {quantity} is not greater or equal to zero!"
        
        # Assign to self object
        self.name = name 
        self.price = price
        self.quantity = quantity

        # Action to execute
        Item.all.append(self)

    def total_price(self):
        return self.price * self.quantity
    def discount(self):
        self.price = self.price * self.pay_rate
    
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

        
    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity} )"  
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price},{self.quantity})"
    
   
    # Inheritance class 
    

class phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function  have access the all attribute / Method 
        super().__init__(name, price, quantity)

        # the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to zero!"
        
        # Assign to self object 
        self.broken_phones = broken_phones


phone1 = phone("Apple", 12000,5,1)

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)