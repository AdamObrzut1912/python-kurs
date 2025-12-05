numbers = [7,8,9,10,11,12]
tupleNumbers = tuple(numbers)
print(tupleNumbers)

mixedList = ["bleble", 123, 12.54]
print(mixedList)

setMix = set(mixedList)
print(setMix)

frozensetNumbers = frozenset(tupleNumbers)

nameAgePairs = (("Adam", 23), ("Niko" , 13), ("Marek", 19))

ageDict = dict(nameAgePairs)
print(ageDict)
print(ageDict["Marek"])