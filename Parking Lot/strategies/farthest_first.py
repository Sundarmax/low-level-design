from .parking_strategy import ParkingStrategy
from entities.parking_floor import ParkingFloor
from entities.vehicle import Vehicle

class FarthestFirstStrategy(ParkingStrategy):
    
    def find_spot(self, floors :  list[ParkingFloor], 
                  vehicle : Vehicle):
        for floor in list(reversed(floors)):
            spot = floor.find_available_spot(vehicle)
            if spot is not None:
                return spot
        return None
