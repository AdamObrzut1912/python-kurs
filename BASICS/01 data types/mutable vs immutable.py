#immutable: int, float, bool, str, tuple, frosenset

a = 1
addr1= id(a)
a += 1
addr2 = id(a)
print(addr1)
print(addr2)
print(addr1 == addr2)


#mutable type: list, set, dict
listData = [0,1,2]
addr1 = id(listData)

listData += [3,4,5]
addr2 = id(listData)

print(addr1 == addr2)
