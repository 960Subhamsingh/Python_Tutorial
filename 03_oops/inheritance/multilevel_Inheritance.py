# In multilevel inheritance, a child class inherits from a parent class, which in turn inherits from another parent class.
class Grandfather:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show_details(self):
        return f'Name: {self.name}, Age: {self.age}'
        
    def speak(self):
        return 'Grandfather speaks wisely.'

class Father(Grandfather):
    def __init__(self, name, age, occupation):
        super().__init__(name, age)
        self.occupation = occupation
        
    def show_occupation(self):
        return f'Occupation: {self.occupation}'
    
    def speak(self):
        return 'Father speaks carefully.'

class Child(Father):
    def __init__(self, name, age, hobby):
        super().__init__(name, age, 'Engineer')
        self.hobby = hobby
        
    def show_hobby(self):
        return f'Hobby: {self.hobby}'
    
    def speak(self):
        return 'Child speaks excitedly.'

child_obj = Child('subham' ,16,'Java')
print(child_obj.show_details())
print(child_obj.show_occupation())
print(child_obj.show_hobby())