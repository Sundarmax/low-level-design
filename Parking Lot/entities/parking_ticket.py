
from .vehicle import Vehicle
from .parking_spot import ParkingSpot
import uuid
import time

class ParkingTicket:

    def __init__(self, vehicle: Vehicle, spot: ParkingSpot  ):
        self.ticket_id = uuid.uuid4()
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = int(time.time() * 1000)  
        self.exit_time =  0
    
    def get_ticekt(self) -> str:
        return self.ticket_id
    
    def get_vehicle(self) -> Vehicle:
        return self.vehicle

    def get_spot(self) -> ParkingSpot:
        return self.spot

    def get_entry_time(self) -> int:
        return self.entry_time
    
    def get_exit_time(self) -> int:
        return self.exit_time
    
    def set_exit_time(self):
        self.exit_time = int(time.time() * 1000)  
        