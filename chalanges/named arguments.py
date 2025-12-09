def createUserProfile(firstName, lastName, age, city):

    slownik = {
        "imie" : firstName,
        "naziwsko" : lastName,
        "wiek" : age,
        "miasto" : city
    }

    return slownik

imie = input("podaj imie")
nazwisko = input("podaj naziwsko")
wiek = input("podaj wiek")
miasto = input("podaj miasto")

dane = createUserProfile(firstName=imie, lastName=nazwisko, age=wiek, city=miasto)

print(dane)