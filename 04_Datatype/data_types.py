
# Basic types in python!

print(type("Hello, world!"))   # This value is represented by string class
print(type(13))                # This value is represented by int class
print(type(4.72))              # This value is represented by  float class
print(type(True))              # This value is represented by  bool class


# Moving to integers
print(432.72, int(432.72))  # Python rounds down!
print(4.4505, int(4.45005))

# Rounding up!
print(4.79, int(4.872), int(round(4.72)))

# Moving strings to integers
print("12665", int("16645"))

# Moving to floats
print(float(168))
print(float("1266345"))

# Moving to strings
print(str(168))
print(str(169.5))
print(type(str(196.5)))

# Logical Operators
# There are four different logical operators; 'and', 'or', 'not' , 'in'

x = 6
print(x > 0 and x < 5)

y = 248
print(y % 2 == 0 or y % 5 == 0)


Fruit = ("Apples", 4, "Bananas", 5, "Oranges", 6, "cherry" ,5)

if 4 not in  Fruit:
    print("is not  available ")
else:
    print("is availabe")


if 4 not in  Fruit:
    print("is availabe")

    