# Print one message if the try block raises a NameError and another for other errors:
try:
    print(x)
except NameError:
    print("x not defined")
except:
    print("Something went wrong")