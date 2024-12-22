
"""
List comprehensions are Python functions that are used for
 creating new sequences
"""
t_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
even_set = {x for x in  t_list if x % 2 == 0}

print(even_set)


even_generator = (x for x in t_list if x % 2 == 0)
for even in even_generator:
    print(even)

list = []

for i in range(1,12):
    sqr = i**2
    list.append(sqr)
    print(list)


# with list comprehension
list1 = [int**2 for int in range(1, 10)]
print('List of sqr using list comprehension: {}'.format(list1))