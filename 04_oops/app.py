class Car:
    totalCar=0
    def __init__(self,brand ,name):
        self.__brand=brand
        self.__name=name
        Car.totalCar+=1

    def get_brand(self):
        return self.__brand +" !"

    def fullName(self):
        return f"{self.__brand} {self.__name}"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"

    def fuelType(self):
        return "Petrol "+"Diesel"
    
    @property
    def model(self):
        return self.__name
    
class ElectricCar(Car):
    def __init__(self, brand, name ,batterysize):
        super().__init__(brand,name)
        self.battersize=batterysize
    
    def fuelType(self):
        return "Electric"


my_car=Car("Toyota","Corolla")
# print(my_car.__brand)
print(my_car.fullName())

tesla=ElectricCar("Tesla","ModelS","85KWh")
print(tesla.fullName())
print(tesla.get_brand())
print(tesla.fuelType())
print(isinstance(tesla,Car))

safari=Car("Tata","Safari")
print(safari.fuelType())
print(Car.totalCar)

#static method using the class
print(Car.general_description())