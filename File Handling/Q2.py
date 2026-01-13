# Close the file when you are finished with it:
with open("demofile.txt") as f:
    print(f.readline())
f.close()