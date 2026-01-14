class Person():
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city
        print("Person constructed")

    def printPersonData(self):
        print("Person.printPersonData: ", self.name, self.surname, self.city)

person1 = Person("Ola", "Kowalska", "Kraków")
person1.printPersonData()

class Employee(Person):
    def __init__(self, name, surname, city, companyName, salary):
        Person.__init__(self, name, surname, city)
        self.companyName = companyName
        self.salary = salary

        print("employee constructor!")

    def printEmployeeData(self):
        print("Emploee.printEmployeeData: ", self.name, self.surname, self.companyName, self.salary)

print()
employee1 = Employee("Kasia", "Kot", "Waw", "TEch LTD", 20000)
employee1.printPersonData()
employee1.printEmployeeData()


class Manager(Employee):
    def __init__(self, name, surname, city, companyName, salary, department):
        Employee.__init__(self, name, surname, city, companyName, salary)
        self.department = department
        print("manager constructor!")

    def hireEmployee(self):
        print("hire employee")
    
    def printManagerData(self):
        print("Manager data: ", self.name, self.surname, self.department)

print()
manager1 = Manager("Ania", "X", "Waw", "Tech 2 LTD", 15000, "IT")
manager1.printPersonData()
manager1.printEmployeeData()
manager1.printManagerData()
manager1.hireEmployee()