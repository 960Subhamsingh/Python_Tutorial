#  Write a Program  to check if a string contains only digits.

name = input("Enter the character : ")

name1 = name.isdigit()

if(name1==True):
    print("It contain only digit")
else:
    print("It not contain digit")