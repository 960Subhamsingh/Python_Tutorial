name = str(input("Enter the name : "))
friends = ["Subham", "Kumar", "Singh", "Mohsn", "sita", "Ram"]
if(name not in friends):
     raise ValueError(f"{name} Not Found")
else:
      print(f"Found {name}")

      