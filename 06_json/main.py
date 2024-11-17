import pprint
import json

with open("D:/Project/Python_Tutorial/06_json/house.json","r")as f:
    data = json.load(f)

print(data)
pprint.pprint(data, width=40)

