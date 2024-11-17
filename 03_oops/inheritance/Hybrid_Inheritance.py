# Hybrid inheritance is a combination of two or more types of inheritance. It allows for complex relationships between classes.

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

class Mother:
    def __init__(self, name, favorite_food):
        self.name = name
        self.favorite_food = favorite_food
        
    def show_favorite_food(self):
        return f'Favorite Food: {self.favorite_food}'
        
    def speak(self):
        return 'Mother speaks lovingly.'
    
class Child(Father,Mother):
    def __init__(self, name, age, favorite_food , hobby):
        Father.__init__(self,name, age, 'Enginner')
        Mother.__init__(self,name,favorite_food)
        self.hobby = hobby
    def show_hobby(self):
        return f"Hobby: {self.hobby}"
    def speak(self):
        return "Child speaks excitedly."
    

child_obj = Child('kumar',18,'Bread','Programing')
print(child_obj.show_hobby())
print(child_obj.show_favorite_food())
print(child_obj.show_occupation())
print(child_obj.show_hobby())
print(child_obj.speak())
 
