num1= int(input("Enter the first Number : "))
num2 = int(input("Enter the Second number : "))

string = "Good"
try:
    print("Inside try block ")

    print("Division is : " , num1/num2)
    try:
        print("Values of String is : " , int(string))
    except ValueError as e:
        print("invalid Input : ")
except ZeroDivisionError as e:
    print("Division by zero is not Possible :", e)