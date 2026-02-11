
from abc import ABC,abstractmethod
from entities.parking_floor import ParkingFloor
from entities.vehicle import Vehicle
class ParkingStrategy(ABC):
    
    @abstractmethod
    def find_spot(self, floors :  list[ParkingFloor], 
                  vehicle : Vehicle):
        pass