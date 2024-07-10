# string are the store  of sequance  of character 

# Operations on strings
# Addition sign concatenation
Greeting = "Hello"
Name = "Ellie"
print(Greeting + Name)

# * Operator
print(Greeting*3)
print(Greeting + Name*3)
print((Greeting + Name)*3)


# Index Operator
Name = "Brad"
print(Name[2])
print(Name[0] + Name[3])


# slicing  Strings

print(Name[0:4])
print(Name[:4])
print(Name[4:])

# Lowercase and Uppercase
name = "Subham"
print(name.lower())
print(name.upper())   # uppper method will conver the upper case of the given string


# Count how many times a character appears in a string

print(name.count("i"))

# Replace specific characters with other characters

print(name.replace("k","d"))

#  Finding the length of String

print(len(name))

# Fomat Method
Input_name = str("your name")
hello = "Hello {}".format(Input_name)
print(hello)

# Each letter in python is assigned to a specific number!

print("orange" < "strawberry")
print(ord("o"))
print(chr(78))

# we can perform  maths on Strings !

# in and not opetators

fruit = "bananas"
print("a" in fruit)
print("s" not in fruit)


# i have create two variable , if one is empty variable another is pre-defined

x = 'Hello'
y = ""

for num in x:
    y = num.upper()+y
    print(y)
