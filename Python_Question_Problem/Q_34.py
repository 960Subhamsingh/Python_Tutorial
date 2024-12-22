#  write a program to find max and min  in a set

t2 = {1, 5, 7, 9, 3}

print(max(t2))
print(min(t2))

# Write a program to find common elements in three lists usings sets

t1 = {1, 12, 7, 34, 23}
t2 = {1, 5, 34, 9, 3}
t3 = {1, 34, 7, 54, 3}

print(set(t1) & set(t2) & set(t3))



# Write a program to find difference between  two sets

t1 = {1, 2, 3, 4, 5}
t2 = {1, 5, 34, 9, 3}

print(t2.difference(t2))


#  Write a Python program to remove an item from a set if it is  present  in the set.

t1 = {1, 12, 7, 34, 356}

print(t1.discard(7))


#  Write a program to check if a set is a suset of another set.

a = {1,2,3,4,5,6}
b = {2,3,4}
print(b.issubset(a))