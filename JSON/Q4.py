# Convert a Python object containing all the legal data types:
import json

x = {
  "name": "Harshit",
  "age": 20,
  "married": False,
  "divorced": False,
  "children": ("A","B"),
  "pets": None,
  "cars": [
    {"model": "Audi 230", "mpg": 27.5},
    {"model": "Ford Escalade", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4, separators=(". ", " = "),sort_keys=True))
