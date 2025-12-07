#Q16: The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the \"Avengers\""
a = "I\'m Ironman"
b = "We can use \\n to print in new line"
c = "How are you?\rThis will overwrite the line"
d = "Hello\tWorld"
e = "Hello\bWorld"
f = "This is idk what\f this does" # form feed character
g = "\123\102" #Octal Value
h = "\x48\x65\x6C\x6C\x6F" #Hexadecimal Value
print(txt)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)