# Loop through the keys and values of all nested dictionaries:

child1 = {
  "name" : "Me",
  "year" : 2005
}
child2 = {
  "name" : "You",
  "year" : 2004
}
child3 = {
  "name" : "Who",
  "year" : 2000
}

family = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

for x, obj in family.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])