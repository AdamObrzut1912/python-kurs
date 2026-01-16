class Vehicle:
    def __init__(self,brand,name):
        self.brand = brand
        self.name = name
        self.__gears = 5 #prywatna zmienna

    def __getGearsInfoStr(self):
        return "gears number" + str(self.__gears)
    
    def printInfo(self):
        print(self.brand, self.name, self.__getGearsInfoStr())


vehicle1 = Vehicle("Dodge", "Charger")
# print(vehicle1.__gears) błąd
# vehicle1.__getGearsInfoStr() błąd

vehicle1.printInfo() # działa bo jest przez pośrednią funkcję
print(vehicle1._Vehicle__gears) # da się odwołać przez ucieczkę przed Vehicle _
print(vehicle1._Vehicle__getGearsInfoStr()) 

class Car(Vehicle):
    def __init__(self, brand, name):
        Vehicle.__init__(self, brand, name)
        # print(self.__getGearsInfoStr()) # błąd
        print(self._Vehicle__getGearsInfoStr())

car1 = Car("Ford", "Mustang")  #nie można odwołać się do prywanet zmiennej w klasie pochodnej ale działa po _getGearsInfoStr() _Vehicle