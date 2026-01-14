population = (38,83,60,46,120)

population += (21,)

print(len(population))

print(100 in population)


print(population[2])
print(max(population))
print(min(population))

if max(population) > 500:
    print("znaleziono kraj o bardzo dużej populacji")
else:
    print("Wszystkie kraje mają populacje poniżej 500 mln")