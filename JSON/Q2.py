# Convert from Python to JSON:
import json
x = {"name":"Harshit",
     "age":20,
     "Country":"India"
     }
y = json.dumps(x)
print(y)