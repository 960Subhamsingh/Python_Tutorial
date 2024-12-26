def add(numbers):
    if(len(numbers)==1):
        return numbers[0]
    else:
        return numbers[0] + add(numbers[1:])
    

print(add([12,3,45,6,7,8]))