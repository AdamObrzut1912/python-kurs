def dispplayShoppingList(shoppingList):
    for i in shoppingList:
        print(i)

userProductList = []

while True:
    nowyProdukt = input("Podaj nowy artykuł lub zakończ wpisując \"koniec\" ")
    if nowyProdukt == "koniec":
        break
    else:
        userProductList.append(nowyProdukt)

dispplayShoppingList(userProductList)
