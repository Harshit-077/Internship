# Sort a list of tuples by the second element:
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorting = sorted(students, key=lambda x: x[1])
print(sorting)