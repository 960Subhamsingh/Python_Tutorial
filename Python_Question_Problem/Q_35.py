#  Write a function to find maximum of three number s in python

def maximum(a , b, c):
        if(a>b and a>c ):
               print(a ,"a is greater ")
        elif(b>c and b>a):
            print(b, "B is greater")
        else:
              print(c, "is the greater No")

maximum(12,13,45)
