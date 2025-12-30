#Q17: The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
dct = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dct.popitem()
print(dct)