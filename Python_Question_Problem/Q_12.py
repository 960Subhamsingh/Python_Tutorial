# Write a program to create a billing system at supermarket.

while True:
    name= input("Enter the customer name : ")
    total = 0


    while True:
        print("Enter the amount of Quantity")
        amount = float(input("Enter amount : " ))
        Quantity = float(input("Enter Quantity : "))
        total += amount * Quantity
        repeat = input("Do you want to add more items ")
        if(repeat=="no" or repeat == "No"):
            break
    print("-" *40)
    print("Name: " , name)
    print("Amount to be paid ", total )
    print("-"*40)
    print(" Good shop Store")

    repeat1 = input("Do you want to go to next customer  ? (yes/no)")
    if (repeat== "no" or repeat=="No" ):
         break