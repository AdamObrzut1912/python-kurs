#immutable int, float, boool ,string ,frosenset

def modifyStr(strData):
    print(id(strData))
    strData += "!"
    print(id(strData))
    print(strData)

string = "Hello"
print(id(string))
modifyStr(string)

print(string)


# mustable types: list, set, dictionary

def modifyList(listData):
    print(id(listData))
    listData.append(10)
    print(id(listData))

listValue = [0,1,2]

print(id(listValue))
modifyList(listValue)