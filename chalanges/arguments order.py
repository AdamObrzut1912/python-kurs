def bookTickets(band, /, *, rodzajBiletów = "standard", sekcja = "global" ):
    print(band, rodzajBiletów, sekcja)

nazwa = input("podaj nazwe zespołu")
bilet = input("podaj rodzaj biletu")

print(bookTickets(nazwa))
