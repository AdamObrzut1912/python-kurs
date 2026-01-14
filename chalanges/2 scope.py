accountBalance = 0

def addFunds(kwota):
    global accountBalance
    accountBalance += kwota

def withdrawsFunds(kwota):
    global accountBalance
    if accountBalance - kwota <0:
        print("suma środków nie pozwala na wybranie tylu pieniędzy")
    else:
        accountBalance -= kwota

def displayBalance():
    global accountBalance
    print(accountBalance)

while True:
    wybor = int(input("""powiedz co chcesz zrobić (wybierz liczbę)
    1. Dodanie środków
    2. Wypłata
    3. Wyświetl stan konta
    4. Zakończ 
    """))
    if wybor == 1:
        kwota = int(input("Podaj kwotę do wpłacenia"))
        addFunds(kwota)
    elif wybor == 2:
        kwota = int(input("Podaj kwotę do wypłacenia"))
        withdrawsFunds(kwota)    
    elif wybor == 3:
        displayBalance()
    elif wybor == 4:
        break
    else:
        print("błąd")