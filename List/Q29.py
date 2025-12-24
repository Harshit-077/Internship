#Q29: Only accept items that are not "apple":
li = ["apple", "banana", "cherry", "date", "apple", "fig"]
newList = [x for x in li if x != "apple"]
print(newList)