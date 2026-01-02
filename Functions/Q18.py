# Using ** to unpack a dictionary into keyword arguments:
def newf(fna, lna):
  print("Hello", fna, lna)

person = {"fna": "Harshit", "lna": "Sharma"}
newf(**person)