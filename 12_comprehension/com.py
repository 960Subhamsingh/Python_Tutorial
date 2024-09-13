t_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
even_set = {x for x in  t_list if x % 2 == 0}

print(even_set)


even_generator = (x for x in t_list if x % 2 == 0)
for even in even_generator:
    print(even)