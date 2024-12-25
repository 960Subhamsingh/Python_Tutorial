''' 4) This function prints out a multiplication table (where each number is the
   result of multiplying the first number of its row by the number at the top
   of its column). Fill in the blanks so that calling multiplication_table(1, 3)
   will print out:
    1 2 3
    
    2 4 6
    
    3 6 9 '''

for  i in range(1,3+1):
    for j in range(1, 3+1):
        print(i*j, end=" ")
    print()

print("\n")

def mul(start , stop):
    for i in range(start, stop+1):
        for j in range(start, stop+1):
            print(i*j, end=" ")
        print()
mul(1,3)