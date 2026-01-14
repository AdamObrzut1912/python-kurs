from functools import reduce

listNum = [10,20,30,40,50]

sum = reduce(lambda x,y: x+y, listNum)
print(sum/len(listNum))