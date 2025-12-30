#Q3: Duplicate values will overwrite existing values:
dct = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(dct)
print(len(dct))