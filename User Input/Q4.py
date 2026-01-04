# Keep asking until you get a number:
x = True
while x == True:
    y = input("Enter a number:")
    try:
        y = float(y)
        x = False
    except:
        print("Wrong input, please try again.")

print("Ok its a number")