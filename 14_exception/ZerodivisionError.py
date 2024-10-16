def divide(a,b):
    try:
        div = (a/b/ (a-b))
    except ZeroDivisionError as e:
        print("Division by zero is not possible :" , e)
    
    else:
        print("Divsion is :" , div)
        """
        It is always executed after try and except blocks. 
        The finally block always executes after normal termination 
        of try block  or after try block terminates due to some 
        exception.
        """
    finally:
        print("In Finally clause")

divide(12,12)
divide(15,3)
divide(0,1)



try: 
    k = 5//0 # raises divide by zero exception. 
    print(k) 
    
# handles zerodivision exception     
except ZeroDivisionError:    
    print("Can't divide by zero") 
        
finally: 
    # this block is always executed  
    # regardless of exception generation. 
    print('This is always executed')  