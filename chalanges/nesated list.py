nested_list = [
    [1,2,3,4,5,6],
    ["Paweł", "Rafał", "Adam"],
    [1, "Ola", 5,"Karol"]
]

for i in nested_list:
    for v in i:
        print(v)