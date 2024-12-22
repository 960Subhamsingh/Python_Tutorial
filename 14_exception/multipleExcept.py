num1 = int(input("Enter the fisrt number : "))
num2 = int(input("enter the second number : "))

try:
    print("Division is : " , num1/num2)
except ZeroDivisionError as e:
    print("Division by :", e)
except ValueError as e:
    print("Division by zero is not possible  : ", e)
except Exception as e:
    print("Something went wrong : ", e)