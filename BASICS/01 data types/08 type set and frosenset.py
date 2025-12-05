setData = {2,3,1,4,5}
setData.add(22)
setData.discard(1)
print(type(setData))
print(setData)

for v in setData:
    print(v)

frosenData = frozenset(set(setData))
print(type(frosenData))

# frosenData.add(56)

for value in frosenData:
    print(value)