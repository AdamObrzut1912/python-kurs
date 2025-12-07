
for v in [1,2,3,4]:
    print(v *2)

for v in ("Ania", "Ola", "Rafał"):
    print(v)

for el in {3,4,5,6,"Ola"}:
    print(el)

for v in "Hello":
    print(v)
else:
    print("pętla zakończona")

dictionaryData = {
    "Ania":"aniaexample.com",
    "Adam":"adamexample.com"
}

for key in dictionaryData.keys():
    print(key)

for key in dictionaryData.keys():
    print(dictionaryData[key])

for key, value in dictionaryData.items():
    print(key,":",value)

for v in dictionaryData.values():
    print(v)
