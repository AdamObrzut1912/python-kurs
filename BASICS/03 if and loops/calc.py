num = 0
operation = None
reset = True
result = None
calcOperations = ["+", "-", "*", "/", "**"]

while True:
    if reset == True:
        num = int(input("Podaj liczbę startową"))
        reset = False

    operation = input(f"Podaj operację arytmetyczną jak np{calcOperations} lub exit jeśli koniec lub reset")

    if operation == "exit":
        break
    if operation == "reset":
        reset = True
        continue

    if not operation in calcOperations:
        print("Wprowadzona została błędna operacja")
        continue

    secondNum = int(input("Podaj drugą liczbę: "))

    if operation == "+":
        result = num + secondNum

    if operation == "-":
        result = num - secondNum

    if operation == "*":
        result = num * secondNum

    if operation == "/":
        result = num / secondNum

    if operation == "**":
        result = num ** secondNum

    print(f"wynik operacji {num} {operation} {secondNum} to {result}")

    num = result
    result = None