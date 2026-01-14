import math
liczba = int(input("podaj liczbę: "))

def calculateAreaSquare(height):
    area = pow(height,2)

    return area

print(calculateAreaSquare(liczba))

liczbaDziesietna = float(input("podaj liczbę dziesiętną"))

print(round(calculateAreaSquare(liczbaDziesietna),2))