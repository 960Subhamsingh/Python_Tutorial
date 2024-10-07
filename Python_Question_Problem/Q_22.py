#  write a program to check if a string is palindrome.

name = input("Enter here : ")

rev = name[::-1]

if(name== rev):
    print("It is a palindrone")
else:
    print("It is not palindrone")

