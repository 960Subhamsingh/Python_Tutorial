
'''When you actually construct a building out of the blueprint, it is called as
an `Instance` or `Object` of the class. So, both are related but essential
different terminology.'''

'''Class = Blueprint, Instance = Building'''

# Methods:

'''These are just normal functions, but defined to alter the behavior of your instance or class.
Since they are tied to a class, they are called as methods. Their behavior is dependent on
the structure you define in the class.'''

# When to use Class:

# Use classes only when you need `Structure` and `Behavior` together.

'''If you only need structure, then choose from any existing data structures such as
list, tuple, dictionary, queue, etc. Just need a behavior? Then just create a function
that transforms your data.'''

### A class in python is the blueprint or template  from which specific objects are created.
"""class Class_Name:
   Statements"""
   
### object-name = class-name.(arguments)   

"""
Some Basic terms for class

1. Class variable  (Attributes) :- class variable is a variable that
 is shared by all the different  objects/instances of a class.

2. Instance/Object  variables :- Instance/Object  variables are 
variables which are unique to each instance. It is defined inside a
 method and belongs only to the current instance of a class. Basically  an objects is everything we can see around. for example - A person is an object of Human class.

3. Methods (Behaviour) :- Methods are also called as functions which
 are defined in a class and describes the behaviour of an object.

"""

class Person:
    """
    The __init__() function is called automatically every 
    time the class is being used to create a new object
    """
    def __init__(self, first_name: str , last_name: str, age: int , gender: chr ) -> None:
        '''initializes an instance of class'''
        """self is kind of By-default parameter , If we have a method which takes no arguments, 
        then we still have to have one argument."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
    def my(self):
        print("Hello my name is " + self.first_name + " and my age is " + str(self.age))
    def __repr__(self) -> str:
        '''repetaion of class'''
        return "<class 'person'>"
    def __str__(self) -> str:
        return f'Name: {self.first_name} {self.last_name} Gender: {self.gender} Age:{self.age}'
    def holiday(self):
        print(f"{self.first_name} says Hello programmer ")
        

# create an instance of class/type
p1 = Person("Subham" , "Kumar", 12,"M")
p2 = Person("Kumar", "Subham", 12,"M")

# Using key value pairs
p3 = Person(first_name="Singh" , last_name="singh" , gender="M" , age=24)
 
print(p1)
print(p3)

# Both  object(p1, p2) are different instances of the same class at different memory location

print(f"p1 is located at memory address: {hex(id(p1))}")
print(f"p2 is located at memory address: {hex(id(p2))}")

print(p1.__str__())
p1.holiday()
p1.my()
