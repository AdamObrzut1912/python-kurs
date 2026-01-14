class Vehicle:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name
        self.__gears = 6

    def _getGearsInfoStr(self):
        return "gears number " + str(self.__gears)
    
    def printInfo(self):
        print(self.brand, self.name, self.__getGearsInfoStr())


veicle1 = Vehicle("Dodge", "Charger")
# print(vehicle1.__gears) błąd
# veicle1.__getGearsInfoStr błąd

veicle1.printInfo()