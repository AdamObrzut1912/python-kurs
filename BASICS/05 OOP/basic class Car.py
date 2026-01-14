class Car:
    def __init__(self, brand, name, color, year):
        self.brand = brand
        self.name = name
        self.color = color
        self.year = year
        self.milage = 1 
        self.setTopSpeed(230)
        self.printInfo()
        

    def printInfo(self):
        print(self.brand, self.name, self.color, self.TopSpeed, self.year, self.milage)

    def setTopSpeed(self, topSpeed):
        self.TopSpeed = topSpeed


mustang = Car("Ford", "Mustang", "red", 1970)
mustang.milage = 100
mustang.setTopSpeed(235)
mustang.printInfo()


charger = Car("Dodge", "Charger", "Blue", 1971)
# print(charger.topSpeed) error
charger.setTopSpeed(232)
charger.printInfo()