
temperatury = []

min_max_srednia = ()
while True:
    wprowadzonaTemperatura = (input("podaj temperaturę lub zakończ poprzez wpisanie \"ZAKONCZ\""))
    if wprowadzonaTemperatura == "zakoncz":
        break

    wprowadzonaTemperaturaFloat = int(wprowadzonaTemperatura)
    temperatury.append(wprowadzonaTemperaturaFloat)

def analizaTemp(temperatury):
    min_max_srednia += min(temperatury)
    min_max_srednia += max(temperatury)
    srednia = 0
    suma = sum((temperatury))
    srednia = suma/len(temperatury)

    min_max_srednia += srednia

    return f"Minimalna to{min_max_srednia[0]}\nmaxymalna to {min_max_srednia[1]}/nsrednia to {min_max_srednia[2]}"


analizaTemp(temperatury)