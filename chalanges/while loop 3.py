liczbaElementow = int(input("Podaj liczbę elementów z których ma być obliczona średnia"))
sum = 0
licznik = liczbaElementow

if liczbaElementow != 0:
    while licznik > 0:
        liczba = int(input("podaj liczbę do dodania"))
        sum += liczba
        licznik -= 1
    srednia = sum / liczbaElementow
    print(float(srednia))
else:
    print("nie można policzyć średniej z 0 elementów")