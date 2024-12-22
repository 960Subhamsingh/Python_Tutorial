num1 = int(input("Enter the fisrt number : "))
num2 = int(input("enter the second number : "))

try:
    print("Division is : " , num1/num2)
except ZeroDivisionError as e:
    print("Divsion by zero is not possible :" , e)
finally:
    print("A is Greater than B" if(num1>num2) else "B is Greater then A")