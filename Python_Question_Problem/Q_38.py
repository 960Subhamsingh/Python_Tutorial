#  Write a Python function to sum all the numbers in a list.


def add(number) :
    total = 0
    for i in number:
        total = total+i
    return total
    
print(add([12,3,4,5,6,74]))