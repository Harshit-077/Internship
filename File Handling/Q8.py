# Open the file "demofile.txt" and overwrite the content:
with open("demofile.txt","w") as f:
    f.write("Reset: this is over written part")
    f.close()
with open("demofile.txt") as f:
    print(f.read())