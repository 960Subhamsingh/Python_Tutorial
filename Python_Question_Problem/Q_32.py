#  Write a program to multiply all the items in a dictionary.

num = {"a":1, "b":2 , "c":3, "d":4 , "e":5}

p = 1

for i in num:
    p*=num[i]

print(p)