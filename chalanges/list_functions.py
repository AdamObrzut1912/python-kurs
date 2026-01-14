import math
guests = ["Rafał","Ola","Kasia","Adam","Marek"]

print(f"ilość gości to {len(guests)}")

guests.append("Piotr")
guests.append("Paweł")


guests.remove("Ola")

guests.sort()
print(guests)

dishes = ["pierogi", "kotlety", "ziemniaki"]

dishes.extend(["kapusta", "twaróg"])
print(dishes[math.floor(len(dishes)/2)])

dishes.pop()

if "pizza" in dishes:
    print("pizza jest na liście")
else:
    dishes.append("pizza")
    print(dishes)