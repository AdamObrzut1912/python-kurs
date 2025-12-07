# operatory logiczne

print(True and True) # True
print(True and False) # False
print(False and False) # False
print(False and True) # False


print(10 >= 5 and 3 < 9) # True
print(12 < 20 and 5 > 10) #False
print( 3==5 and 6 < 1) #False

taskCompleted = True
linesOfCodeWritten = 100

if(taskCompleted == True and linesOfCodeWritten >= 50):
    print("go home!")

hourOfDay = 15
if taskCompleted == True and linesOfCodeWritten >= 60 and hourOfDay >= 15:
    print("go home!")

#or
print(True or True) #True

print(True or False) #True

print(False or False) #False

print(10 >= 10 or 5 > 3) #True

print(5 <= 7 or 5==1) #True

print(2 != 2 or 5 == 5) #True

print(1 == 3 or 4 > 10) #False


if (10 > 5 or "Ania" != "Ola"):
    print("True or True")

if 3 == 5 or "Ania" == "Ola":
    print("false or false")


#not

print(not True) #False

print(not False) #True

print(not (3 == 3)) #False

print(not(5 > 10))

print(not (10 >= 6 and "Ola" != "Ania"))

taskCompleted = True

if taskCompleted == True:
    print("Go home")

if not taskCompleted:
    print("stay a bit longer and finish")

