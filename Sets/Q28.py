#Q28: Use the difference_update() method to keep only the items from the first set that are not present in the other set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)