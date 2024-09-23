def divide(a,b):
    try:
        div = a/b
    except ZeroDivisionError as e:
        print("Division by zero is not possible :" , e)
    
    else:
        print("Divsion is :" , div)
    finally:
        print("In Finally clause")

divide(12,5)
divide(15,3)
divide(0,1)