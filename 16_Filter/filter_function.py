# The filter function is an inbuilt function in python
# that takes in two arguments - a boolean_function & an iterator

# syntax - filter(boolean_function,iterator)

# the filter function returns a filter of the results
# that returns true for
# each element in the iterable


nums = [1, 6, 7, 9, 4, 12,13,15,17, 19, 21,23,25,24,26,28]


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


result = filter(is_even, nums)

print(list(result))


# check ood number

def is_odd(x):
    if x % 2 == 0:
        return False
    else:
        return True
result1 = filter(is_odd,nums)
print(list(result1))

def check_odd(num):
    return num % 2 != 0


mynums = [1, 2, 3, 4, 5]

result = filter(check_odd, mynums)
print(list(result))


