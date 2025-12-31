# Checking multiple conditions with nesting:
age = 25
eligible = True

if age >= 18:
    if eligible:
        print("You can drive")
    else:
        print("You need a license")
else:
  print("You cannot drive")