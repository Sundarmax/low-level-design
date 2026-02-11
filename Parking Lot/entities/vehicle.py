
from enums.vehicle_size import VehicleSize
from abc import ABC

class Vehicle(ABC):

    def __init__(self, license_number : str, vehicle_size : VehicleSize):
        self.lic_number = license_number
        self.size = vehicle_size
    
    def get_license_number(self) -> str:
        return self.lic_number

    def get_size(self) -> VehicleSize:
        return self.size

class Bike(Vehicle):

    def __init__(self, license_number):
        super().__init__(license_number, VehicleSize.SMALL)

class Car(Vehicle):
    
    def __init__(self, license_number):
        super().__init__(license_number, VehicleSize.MEDIUM)

class Truck(Vehicle):
    
    def __init__(self, license_number):
        super().__init__(license_number, VehicleSize.LARGE)
