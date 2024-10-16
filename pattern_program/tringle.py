num = int(input("Enter the number :"))
for i in range(1, num+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()


num = int(input("Enter the number :"))
for i in range(1, num+1):
    for j in range(1, i+1):
        print("1", end=" ")
    print()   

for i in range(1,5):
    for j in range(i):
        print(i, end=" ")
    print()