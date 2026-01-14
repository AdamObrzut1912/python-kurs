from functools import reduce

users = [
    {"name":"Jan", "age":15},
    {"name:": "Anna", "age":25},
    {"name:": "Piotr", "age":30},
    {"name:": "Katarzyna", "age":22}
    
]

over18 = list(filter(lambda x: x["age"] > 18, users))

print(over18)

doubleAge = list(map(lambda x: x["age"]*2, over18))

reduced = reduce(lambda x,y: x + y, doubleAge)

print(reduced)

