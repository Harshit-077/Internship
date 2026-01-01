# Sending a dictionary as an argument:
def func(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

data = {"name": "Emil", "age": 25}
func(data)