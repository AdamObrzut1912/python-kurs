def calculateHumanYears(dogAge):

    humanAge = None
    if int(dogAge) <= 2:
        humanAge = int(dogAge) * 10.5
    elif int(dogAge) > 2:
        humanAge = 21 + (int(dogAge) -2)*4
    return humanAge


while True:
    danaWejsciowa = input("Podaj wiek psa lub wprowadź \"zakończ\" żeby wyjść")
    if danaWejsciowa == "zakończ":
        break

    print(calculateHumanYears(danaWejsciowa))