def add(x):
    return x* x
print(add(12))

# add a number in x variable
add_num = lambda x: x+12
print(add_num(24))


# map(function , iteration)

def square(y):
    return y*y

numbers = [1,2,3,4,5,6]

s_number = map(square, numbers)
 
y = list(s_number)
print(y)


square_num = map(lambda x: x*x, numbers)
g = list(square_num)
print(y)


# filter(function , iterable )

# Codeium: Refactor | Explain  | Generate Docstring|X

def even_Num(x):
    return x%2 == 0
number = [1,2,3,4,5,6,8,10,12,24,26,25,23]
z = filter(even_Num , number)
n = list(z)
print(n)


f_lambda = filter(lambda x: x%2==0,number)
s = list(f_lambda)
print(s)

num= list(range(1,11))
s_even_num = map(lambda x: x*x, filter(lambda x: x%2==0 , num))
a = list(s_even_num)
print(a)


new_tup = tuple(filter(lambda x:(x%3==0), number))
print(new_tup)
