data = { "name":"Ola", "City":"Waw"}
print(data["name"])
dataPostalCode = "postalCode"
data[dataPostalCode] = "12345"
print(data)

print(len(data))


del data["City"]
print(data)
data.clear()

data = {"name": "Kasia", "city":"Krk"}
dataCopy = data.copy()
print(data["name"] is dataCopy["name"])
print(data is dataCopy)

data2 = dict.fromkeys(("name", "city", "code"),)
data3 = dict.fromkeys(("name", "city", "code"),0)
print(data3)

print( data2.get("x", "DEFAULT") )

print("name" in data2)
print(data2.keys()) 
print(data2.values()) 

