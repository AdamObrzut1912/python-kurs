def increaseSalary(money,bonus):
    money *= 0.80

    return money, bonus

salary = 5000

newSalary = increaseSalary(salary,1000)

print(salary)
print(newSalary)