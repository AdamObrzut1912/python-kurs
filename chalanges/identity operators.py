tekst = "Hello"
print(tekst.upper())
print(dir(tekst))

x= 256
y = 256
print(x is y)

listOne = [1,2,3,4,5,6]

listTwo = listOne
print(listOne is listTwo)

listOne.append(99)

if listOne is listTwo:
    print("lista1 jest listą 2")
else:
    print("lista 1 nie jest listą2")

listThree = [1,2,3,4,5,6,99]

if listOne is listThree:
    print("lista 1 jest listą 3")
else:
    print("lista 1 nie jest listą 3")