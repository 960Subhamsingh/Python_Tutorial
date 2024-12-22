menu = {
    'Pizza ': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad' : 70,
    'Coffee': 80,
}

print("Welcome to Restaurant")
print("Pizza : Rs40\nPasta: Rs50\nBurger: Rs60\nSalad: Rs70\nCoffee: Rs80")

Total_order = 0

item = input("Enter the name of item you want to order =")

if(item in menu):
    Total_order +=menu[item]
    print(f"your item {item} has been added to your order")
else:
    print(f"Order item {item} is not available yet ")

another_order = input(" Do you want to add another items? (Yes/No)")
if(another_order == "Yes"):
    item_2 = input("Enter the name of second item = ")
    if(item_2 in menu):
        Total_order +=menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print("ordered item {item_2} is not avaialble!")
print(f"the total amount of item to pay is {Total_order}")