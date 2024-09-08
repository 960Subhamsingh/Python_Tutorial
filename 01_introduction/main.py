
x = [1,2]
y=x
x[0]= 100


def num(numbers, n):
    numbers.sort()
    return numbers[-n:]

num = [2,3,4,5,134,123,321,1]

print(num)

largest = sum(num,2)
print(largest)