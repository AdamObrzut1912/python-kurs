dogAge = float(input("Podaj wiek psa"))
humanAge = 0

if dogAge < 0:
    print("error")
elif dogAge <= 1:
        humanAge += dogAge * 15
elif dogAge <= 2:
        humanAge += 15 + (dogAge-1)*9
else:
    humanAge = 24 + (dogAge-2)*5

print(f"wiek psa w ludzkich latach to {humanAge}")
