a = [1, 2, 3, 4, 5,6,7,8,9,10]

try:
    print("element = %d" %(a[1]))
    #Throws error since there are only 4 elements in array
    print("Fourth element = %d" %(a[10]))
except IndexError:
    print("an error occurred")
