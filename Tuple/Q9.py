#Q9: Convert the tuple into a list to be able to change it

tup = ("apple","banana","cherry")
y = list(tup)
y[1] = "guava"
tup = tuple(y)
print(tup)