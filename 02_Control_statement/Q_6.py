#  Write a program to check if a number  is a single digit number, 2-digit number and so on .. up to 5 digits.


num = int(input("Enter a number "))

if(num>=0 and num<=9):
    print("It is single digit number")
elif (num>=10 and num<=99):
    print("It is a double digit number")
elif (num>=100 and num <=999):
    print("It is tree digit number")
elif(num>=100 and num<=9999):
    print("It is four digit number")

elif (num>=1000 and num<=9999):
    print("It is a four digit number")

else:
    print("It is given five digit number")