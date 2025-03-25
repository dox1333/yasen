# very simple proj
import json


with open("proj.json", "r") as f:
     data = json.load(f)
     print(data)
