liczbaN = int(input("Podaj liczbę do której chcesz wyświetlić kwadraty poprzednich list"))
even = []
odd = []
for i in range(1,liczbaN + 1):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)
