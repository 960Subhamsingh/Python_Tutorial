class Item:
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"
        # Assign to self object 
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total(self):
        return self.price * self.quantity

item1 = Item("Phone", 10500, 12)
item2 = Item("Laptop" , 2000,2)

print(item1.calculate_total())
print(item2.calculate_total())