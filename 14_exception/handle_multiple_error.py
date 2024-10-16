# Program to handle multiple errors with one except statement


try : 
    a = 3
    if a < 4 :
  
        # throws ZeroDivisionError for a = 3 
        b= a/(a-3)
        print("Values of b = ", b )
        c = a/(a-3)
        # thros NameError if a>=4
        print("Values of b = ", c )
except (ZeroDivisionError, NameError):
    print("\n Error Occured and Handled")