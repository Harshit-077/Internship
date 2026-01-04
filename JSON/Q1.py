# Convert from JSON to Python:
import json
x = '{"name":"Harshit","age":20,"Country":"India"}'
y = json.loads(x)
print(y['age'])