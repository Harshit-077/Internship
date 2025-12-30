# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
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
print(family)