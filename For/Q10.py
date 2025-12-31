# Break the loop when x is 3, and see what happens with the else block:
for i in range(10):
    if i==3:
        break
    print(i)
else:
    print("The loop ended")