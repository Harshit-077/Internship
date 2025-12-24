#Q33: Return "orange" instead of "banana"
li = ["apple","banana","orange"]
newlist = [x if x != "banana" else "orange" for x in li]
print(newlist)