# Convert the tuple into a list, remove "apple", and convert it back into a tuple:
tup = ("apple","orange","banana")
y = list(tup)
y.remove("apple")
tup = tuple(y)
print(tup)