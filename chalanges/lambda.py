names = ["Ola", "Ania", "Kasia"]
surname = list(map(lambda x: x + " Kowalska", names))
print(surname)

filtered = list(filter(lambda x: len(x)  > 12, surname))
print(filtered)