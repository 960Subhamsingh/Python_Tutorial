#  Write a program to display this patter.

for i in range(1, 10):  # rows
    for j in range(1 , i+1): # columns
        print("*", end=" ")
    print()

print("next Pattern")

for i in range(1, 10):  # rows
    for j in range(1 , i+1): # columns
        print(j, end=" ")
    print()

print("next Pattern")

for i in range(1, 10):  # rows
    for j in range(1 , i+1): # columns
        print(i, end=" ")
    print()

print("next Pattern")

for i in range(1, 10):  # rows
    for j in range(6 ,i ,-1): # columns
        print(i, end=" ")
    print()


print("next Pattern")

for i in range(1, 10):  # rows
    for j in range(6 ,i ,-1): # columns
        print(j, end=" ")
    print()


print("next Pattern")

for i in range(1, 6):  # rows
    for j in range(4 ,i ,-1): # columns
        print(" ", end=" ")
    for k in range(i):
        print("*" ,end=" ")
    print()

print("next Pattern")

for i in range(1, 6):  # rows
    for j in range(1 ,i+1): # columns
        print("*", end=" ")
    print()
print("next Pattern")
for i in range(5,0,-1):  # rows
    for j in range(1 ,i-1): # columns
        print("*", end=" ")
    print()


print("next Pattern")

for i in range(1, 6):  # rows
    for j in range(1 ,i+1): # columns
        print(i*j, end=" ")
    print()