class Grandparent:
    def __init__(self, name, age) -> None:
        self.name = name 
        self.age = age
    def show_detail(self):
        return f"Name: {self.name}, Age: {self.age}"
    def speak(self):
        return " G.f speaks Wisely"

class Father(Grandparent):
    def __init__(self, name, age, occupation) -> None:
        super().__init__(name, age)
        self.occupation = occupation
    def show_occupation(self):
        return f"Occupation: {self.occupation}"
    def speak(self):
        return 'Father speaks carefully.'
    
obj = Grandparent("kumar",12)
print(obj.show_detail())

obj1 = Father("kumar",12,"Engineer")
print(obj1.show_detail())
print(obj1.show_occupation())
print(obj1.speak())