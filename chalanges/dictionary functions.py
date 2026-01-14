addresBook = {
    "Jan Kowalski":{
        "name": "Jan",
        "surname": "Kowalski",
        "city": "Gdańsk",
        "postal code": "80-800"
    }
}

addresBook["Anna Nowak"] = {"name": "Anna", "surname": "Nowak", "city":"Warszawa", "postalCode":"00-001"}

del addresBook["Jan Kowalski"]

copyAddresBook = addresBook.copy()

print(addresBook is copyAddresBook)
print(addresBook == copyAddresBook)

if "Kraków" in copyAddresBook:
    print("jest osoba z krakowa")
else:
    print("nie ma osoby z krakowa")

print(addresBook.items())
