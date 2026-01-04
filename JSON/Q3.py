# Convert Python objects into JSON strings, and print the values:
import json
print(json.dumps({"name": "Harshit", "age": 20}))
print(json.dumps(["Orange", "bananas"]))
print(json.dumps(("apple", "Litchi")))
print(json.dumps("hello"))
print(json.dumps(39))
print(json.dumps(129.24))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))