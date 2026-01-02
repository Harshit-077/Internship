# Accessing values from **kwargs:
def val(**data):
    print("Type:", type(data))
    print("Name:", data["name"])
    print("Age:", data["age"])
    print("All data:", data)


val(name="Harshit", age=20, city="Chandigarh")