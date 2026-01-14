class Vehicle:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name
        self.topSpeed = 10
        self.numWheels = 4

    def printVehicleInfo(self):
        print("vehicleInfo", self.brand, self.name, self.numWheels, self.topSpeed)

    def printNumWheels(self):
        print("Vehicle.numWheels: ", self.numWheels)
        

vehicle1 = Vehicle("Vehicle", "basic")
vehicle1.printVehicleInfo()


class Car(Vehicle):
    
    def printCarInfo(self):
        self.topSpeed = 240
        print("PrintCarInfo: ", self.brand, self.name, self.topSpeed, self.numWheels)

    def printVehicleInfo(self):
        print("Car.vehicleInfo", self.brand, self.name, self.numWheels, self.topSpeed)
        

car1 = Car("Ford", "Mustang")
car1.printCarInfo()
car1.printVehicleInfo()
car1.printNumWheels()

class SuperCar(Car):
    def reachSpeed300(self):
        self.topSpeed= 301
        print("Super car reached 300!")
    


superCar1 = SuperCar("Ford", "GT")
superCar1.reachSpeed300()
superCar1.printVehicleInfo()
superCar1.printNumWheels()