
from enums.vehicle_size import VehicleSize
from .vehicle import Vehicle

class ParkingSpot:

    def __init__(self,spot_id : str, spot_size : VehicleSize):
        self.spot_id = spot_id
        self.spot_size = spot_size
        self.is_occupied = False
        self.parked_vehicle = None

    def get_spot_id(self) -> str:
        return self.spot_id

    def get_spot_size(self):
        return self.spot_size

    def is_occupied_spot(self) -> bool:
        return self.is_occupied
    
    def is_availble(self) -> bool:
        return self.is_occupied

    def park_vehicle(self, vehicle: Vehicle):
        self.is_occupied = True
        self.parked_vehicle = vehicle

    def unpark_vehicle(self):
        self.is_occupied = False
        self.parked_vehicle = None
    
    def can_fit_vehicle(self, vehicle : Vehicle):
        
        if self.is_occupied:
            return False
        
        if vehicle.get_size() == VehicleSize.SMALL:
            return self.spot_size == VehicleSize.SMALL
        elif vehicle.get_size() == VehicleSize.MEDIUM:
            return self.spot_size == VehicleSize.MEDIUM
        elif vehicle.get_size() == VehicleSize.LARGE:
            return self.spot_size == VehicleSize.LARGE
        else:
            return False
        
