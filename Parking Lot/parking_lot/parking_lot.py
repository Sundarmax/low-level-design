from entities.parking_floor import ParkingFloor
from strategies.nearest_first import NearestFirstStrategy
from entities.vehicle import Vehicle
from entities.parking_ticket import ParkingTicket
from strategies.parking_strategy import ParkingStrategy
from strategies.fee.flat_rate_fee_strategy import FlatRateFeeStrategy

import threading

class ParkingLot:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        self.floors : list[ParkingFloor] = []
        self.parking_strategy = NearestFirstStrategy()
        self.fee_strategy = FlatRateFeeStrategy()
        self.active_tickets: dict[str, ParkingTicket] = {} 
    
    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            with ParkingLot._lock:
                if ParkingLot._instance is None:
                    ParkingLot._instance = ParkingLot()
        return ParkingLot._instance
    
    def add_floor(self, floor : ParkingFloor):
        self.floors.append(floor)
    
    def set_parking_strategy(self, strgy : ParkingStrategy):
        self.parking_strategy = strgy

    def park_vehicle(self, vehicle : Vehicle ):
        spot = self.parking_strategy.find_spot(self.floors,vehicle)
        if spot is not None:
            spot.park_vehicle(vehicle)
            ticket = ParkingTicket(vehicle, spot)
            self.active_tickets[vehicle.get_license_number()] = ticket
            print(f"Vehicle {vehicle.get_license_number()} parked at spot {spot.get_spot_id()}")
            return ticket
        else:
            print(f"No available spot for vehicle {vehicle.get_license_number()}")
            return None
    
    def unpark_vehicle(self, license_number: str):
        ticket = self.active_tickets.pop(license_number, None)
        if ticket is None:
            print("Ticket not found")
            return None
        ticket.get_spot().unpark_vehicle()
        ticket.set_exit_time()
        fee = self.fee_strategy.calculate_fee(ticket)
        print(f"Vehicle {license_number} unparked from spot {ticket.get_spot().get_spot_id()}")
        return fee