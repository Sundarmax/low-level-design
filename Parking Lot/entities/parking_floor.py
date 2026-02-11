
from .parking_spot import ParkingSpot
from enums.vehicle_size import VehicleSize
from collections import defaultdict
from .vehicle import Vehicle

class ParkingFloor:
    
    def __init__(self,floor_number: int):
        self.floor_number = ""
        self.spots : dict[str, ParkingSpot] = {}
    
    def add_spot(self, spot : ParkingSpot):
        self.spots[spot.get_spot_id()] = spot

    def display_availability(self):
        print(f"-- floor {self.floor_number} availability---")
        available_count = defaultdict(int)

        for spot in self.spots.values():
            if not spot.is_occupied_spot():
                available_count[spot.get_spot_size()] += 1
        for v_size in VehicleSize:
            print(f"{v_size.value} spots: {available_count[v_size]}")         

    def find_available_spot(self, vehicle : Vehicle ):
        available_spot =  [
            spot for spot in self.spots.values()
            if not spot.is_occupied_spot() and spot.can_fit_vehicle(vehicle)
        ]
        if available_spot:
            available_spot.sort(key= lambda x: x.get_spot_size().value)
            return available_spot[0]
        return None