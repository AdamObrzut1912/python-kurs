def calculateArea(length, width):
    surface = length * width
    return surface

dlugosc = int(input("Podaj długość prostokąta "))
szerokośc = int(input("Podaj szerokość prostokąta "))

print(calculateArea(dlugosc, szerokośc))