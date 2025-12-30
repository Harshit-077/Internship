# Add a new item to the original dictionary, and see that the keys list gets updated as well:
dct = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = dct.keys()
print(x)
dct["owner"] = True
x = dct.keys()
print(x)