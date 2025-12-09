import math
import random

print(type(str(12)))
print(type(str([12, 34])))

number = int("123")
print(type(number))


number += 10

print(number)
print("123" + "10")

floatNum = float("45.54")
print(type(floatNum))
floatNum = floatNum *2
print(floatNum)


print(abs(9))
print(abs(-9.1))

print(math.ceil(11.00000001)) #12
print(math.floor(11.00000001)) #10

print(math.ceil(9.999999999)) # -1
print(math.ceil(-1.00000000001)) #-1
print(math.ceil(-1.99999999999)) # -1

print(math.floor(11.000000001)) # 11
print(math.floor(11.999999999)) # 11
print(math.floor(5.12)) # -6
print(math.floor(-5.12)) # -6


print(max(10,1,-9,33,89,0)) #89
print(max((10,1,-9,33,89,0))) #89
print(max([10,1,-9,33,89,0])) #89
print(min(10,1,-9,33,89,0)) # -9

print(4 ** 3) # 64

print(pow(4,3))

print(math.sqrt(128)) # 11.31

print(round(12.7894342, 3))
print(round(12.7894342, 1))


print(int(random.random()*100))

print(random.choice([0,1,2,3,4]))
print(random.choice(["ola", "ania", "adam"]))


print(random.randrange(-10,30,5))

listData = [0,1,2,3,4,5,6]
random.shuffle(listData)
print(listData)

