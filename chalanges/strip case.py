def getUserInformation(name,surname,job):
    name = name.upper().strip()
    surname = surname.upper().strip()
    job = job.lower().strip
    tekst = f"imię: {name}, nazwisko: {surname}, zawód: {job}"
    return tekst

print(getUserInformation("Ania            ", "Kowalska", "Programistka"))
print(getUserInformation("Daniel", "Lis", "Administrator"))


