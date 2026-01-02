# Using *args to accept any number of arguments:
def newfunct(*names):
    print("name:", names[0])
newfunct(["Harshit","Sharma"])