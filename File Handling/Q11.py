# Check if file exists, then delete it:
import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("File does not exist")