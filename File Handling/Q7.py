# Open the file "demofile.txt" and append content to the file:
with open("demofile.txt","a") as f:
    f.write(" Hello, this is the appended part")
    f.close()
with open("demofile.txt") as f:
    print(f.read())