number = 12

def test1():
    print(number) # 12 globalna

test1() #12

def test2():
    number = 100
    print(number) #100

    if 1 == 1:
        print(number) #100
    if 2 == 2:
        number = 50
        print(number) #50
    print(number) #50

test2()#100

print(number) #12

print("\n test3")

def test3():
    global number
    number = 5
    print("test3", number) #5
    if 1 == 1:
        number = 6
        print("test3", number) #6

test3()
print("global number after test 3()", number) #6

print("\n test4()")
number = 10
def test4(number):
    print("test4 param:", number)
    number = 20
    print("test4 after change:", number)

test4(33)

print("number after test4()", number)


print("\n test5()")

number = 10
def foo():
    print("foo number", number)

def bar():
    number = 9
    print("bar() number", number )
    foo()

bar()
print("global number after foo() bar()", number)

print("\n check1 & check2")
number = 10
def check1():
    number = 12
    print("check1() number", number ) #12
    def check2():
        print("check2 number", number) #12
    check2()

check1()
print("global number after check1(): ", number)

print("\n test")

if 1 == 1:
    data = 100 # utworzy zmienną globalną

print("data in global scope ", data)

# if 2 == 1:
#     nextData = 15

# print("nextData in global scope" , nextData) #NameError: name 'nextData' is not defined
