# This is Tuple conventionally 
# Tuple is imuttable . it can not change the change the existing values
# tuple is written by round bracket
Fruit = ("Apples", 4, "Bananas", 5, "Oranges", 6, "cherry" ,5)

# dispally the tuple 
print(Fruit)

# Return the fruit_item position of 1 

print(Fruit[1])

# tuple has only create it will not change , if the existing index
try:
    Fruit[1] = 'blackberry'
except TypeError as e:
    print(e)

# tuple are unchange able eith the 'del' method
try:
    del Fruit[0]
except TypeError as e:
    print(e)

#  to deermine how many item in list have , use then len() method 

print(len(Fruit))

#  Diplay item of index 'one to Five'  with slicing method

print(Fruit[0:5])

# type method are display , which type of object created and which datatype are use

# create  another tuple  

Fruit_2 = list(Fruit)
Fruit_2.append('MAngo')
Fruit = tuple(Fruit_2)

# unpacking the tuple
(one, *two, three, four) = Fruit
print(one, two , three)

#  iterate the  tuple item 
for x in Fruit:
    print(x, end=" ")

#  check that if item is existing

Fruit = ("Apples", 4, "Bananas", 5, "Oranges", 6, "cherry" ,5)

if 4 not in  Fruit:
    print("is not  available ")
else:
    print("is availabe")


if 4 not in  Fruit:
    print("is availabe")