listData = [1,2,3,4,5,6]
tupleData = tuple(listData)
print(tupleData)

otherList = list(("Ola", 23, 234))
print(otherList)

setData = set(otherList)
print(type(setData))
print(setData)

frosenSetData = frozenset(tupleData)
print(type(frosenSetData))
print(frosenSetData)

tupleData = (("Ola", 1234), ("Adam", 23654))

dictData = dict(tupleData)
print(dictData)

print(dictData["Ola"])