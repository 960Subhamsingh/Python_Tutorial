# In hierarchical inheritance, multiple child classes inherit from a single parent class.

class Grandfather:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show_details(self):
        return f'Name: {self.name}, Age: {self.age}'
        
    def speak(self):
        return 'Grandfather speaks wisely.'
    

class child(Grandfather):
    def __init__(self, name, age, hobby):
        super().__init__(name, age)
        self.hobby = hobby
    
    def show_hobby(self):
        return f"Hobby: {self.hobby}"
    def speak(self):
        return 'speaks enthusiastically.'

class child1(Grandfather):
    def __init__(self, name, age, favorite_subject):
        super().__init__(name, age)
        self.favorite_subject = favorite_subject
    def show_favorite_subject(self):
        return f"Favorite Subject: {self.favorite_subject}"
    def speak(self):
        return "speaks thoughtfully"

c = child("kumar",14,"Python leanring")
c1 = child1("sk",15,"Python & Mathematics")
print(c.show_details())
print(c.show_hobby())
print(c1.show_favorite_subject())
print(c1.favorite_subject)

