name = ["subham", "kumar","Singh"]
age = [12,32,12]

 

z = list(zip(name, age))
for name, age in z:
    print(f"{name} is {age} years old ")


for i in range(min(len(name),len(age))):
    name = name[i]
    age= age[i]
    print(f"{name} is {age} years old" )