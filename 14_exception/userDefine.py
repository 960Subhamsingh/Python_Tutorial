print("Exception for checking age is valid for voting or not. ")


class InvalidAgeError(Exception):
    ''' If we use this then we can get e.message as well '''

    def __init__(self, message):
        self.message = message


def checAge(age):
    if age <18:
        try:
            raise InvalidAgeError("You are underage for voting")
        except:
            print("InvalidAgeError : ", InvalidAgeError)
    else:
        print("You are able for voting.")


checAge(int(input("Enter a age : ")))





#-----------------------------------


print(" Exception for checking number is negligible or not. ")

''' Here NumberIsNegligibleException is allow as name but this is not java and in python
    every exception has prefix as Error '''

class NumberIsNegligibleError(Exception):
    pass


def checkNumber():
    print("Enter the value of A and B : ")
    a = int(input())
    b = int(input())
    c = a + b
    t = float(c) / 50000000000
    if(t < 0.00001):
        try:
            raise NumberIsNegligibleError("Number is Negligible")
        except NumberIsNegligibleError as e:
            print("NumberIsNegligibleException : ",e)
    else:
        print("Number is not Negligible")

checkNumber()




print(" Custom Exception for checking subtraction of number is negative or not. ")

class NegativeAnswerError(Exception):
    pass


def checkSubtract():
    print("Enter two numbers for subtraction : ")
    a = int(input())
    b = int(input())
    if a<b:
        try:
            raise NegativeAnswerError("Negative Answer Found")
        except NegativeAnswerError as e:
            print("Subtraction is not possible : ",e)
    else:
        print("Subtraction is : ",a-b)

checkSubtract()