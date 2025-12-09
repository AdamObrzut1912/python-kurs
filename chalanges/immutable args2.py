def calculateFinalPrice(initialPrice, discount):
    priceAfterDiscount = initialPrice - initialPrice*(0.01*discount)
    return priceAfterDiscount

cena = int(input("Podaj początkową cenę"))
znizka = int(input("podaj zniżkę"))

cenaPoRabacie  = calculateFinalPrice(cena,znizka)

print(cenaPoRabacie)