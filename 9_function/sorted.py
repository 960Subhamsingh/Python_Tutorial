people = [
    {"Name": "Subham", "age": 23},
    {"Name": "Kumar" ,"age":23}

]

sorted_people = sorted(people, key=lambda p : p["age"], reverse=True)
print(sorted_people)