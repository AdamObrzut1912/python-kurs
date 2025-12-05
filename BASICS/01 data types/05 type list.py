list = ["Ola", "Ania", 23, 99, "Rafał"]
print(type(list))
print(list)

print(list[0])
print(len(list))
print(list[4])
print(list[len(list)-1])
print(list[-1])
print(list[-2])
# print(list[-6])

print(list[1:4])
print(list[2:])
list[0] = "Kasia"
print(list)
del list[2]
print(list)

print(99 in list)
print("Rafał" in list)
print("Ola" in list)

if "Ania" in list:
    print("Ania jest w liście list")
    print("Kolejny kod")

print("Dalszy kod")

for v in list:
    print(v)


data = [
    ["Daniel", "Rafał"],
    ["Kasia", "Ania"],
    ["Ola", "Adam"] 
 ]

print(len(data))

print(data[1][0])
print(data[0][1])

data1 = [1,2,3]
data2 = [4,5,6]

numbers = data1 + data2
print(numbers)

numbersX2 = numbers * 2
print(numbersX2)