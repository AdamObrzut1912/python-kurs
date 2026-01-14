employees = []

def addEmployee(email, salary):
    slownik = {
        "email":email,
        "salary":salary 
    }
    employees.append(slownik)

addEmployee("coś", 6000)
addEmployee("coś1", 8000)
addEmployee("coś3", 10000)

def increaseSalary(employees, pctIncrease):
    for pearson in employees:
        pearson["salary"] += pearson["salary"] * (pctIncrease /100)

increaseSalary(employees, 20)

print(employees)