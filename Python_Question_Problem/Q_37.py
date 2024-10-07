#  write a Python function that takes a number as a parameter and check if the number is prime or not.

def check(num):
    if(num==1):
        print("It is not a prime number")
    if(num==2):
        print("It is a prime number")
    
    if(num>2):
        for i in range(2, num):
            if(num%i==0):
                print("It is not a prime number")
                break
        else:
            print("It is a primae number")

check(30)