
# Function

# Like in mathematics, where a function takes an argument and produces a result,

# def function_name(arguments):
#   {lines telling the function what to do to produce the result}
#   return result

def squared(x, y):
    result = x**2 + y**2
    return result

print(squared(10, 2))


# A new function
def born(country):

    return print("I am from " + country)


born("BiHar")


 
def pythagorean_triple(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

print(pythagorean_triple(2,3,4))     # This is True
print(pythagorean_triple(3, 4, 5))   # This is True
print(pythagorean_triple(3, 9, 15))  # This is 


