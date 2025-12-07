liczbaN = int(input("podaj do jakie liczby chcesz wyświetlić jej kwadraty"))
liczby = []


for i in range (1,liczbaN+1):
    liczby.append(i**2)

if len(liczby) > 0:
    print(liczby)

