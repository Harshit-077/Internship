# Create a function that converts feet into meters:
def conv(x):
  return x * 0.3048

txt = f"The plane is flying at a {conv(30000)} meter altitude"
print(txt)