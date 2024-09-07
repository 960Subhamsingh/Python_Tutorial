name = ["apple", "mango","Banana"]
length = map(len , name)
print(list(length))

length1 = map(lambda x:x + "s", name)
print(list(length1))

def names(name):
    return name + "s"
length2 = map(names. name)
print(list(length2))

# serial by name data with for loop
for i in range(len(name)):
    task=name[i]
    print(f"{i+1}, {task}")

for i , task  in enumerate(name):
    print(f"{i+1}, {task}")

list(enumerate(name))