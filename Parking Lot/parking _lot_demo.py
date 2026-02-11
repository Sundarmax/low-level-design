from entities.parking_floor import ParkingFloor
from parking_lot.parking_lot import ParkingLot
from entities.parking_spot import ParkingSpot
from enums.vehicle_size import VehicleSize
from entities.vehicle import Bike,Car,Truck

class ParkingLotDemo:

    @staticmethod
    def main():
        parking_lot = ParkingLot.get_instance()

        floor1 = ParkingFloor(1)
        floor1.add_spot(ParkingSpot("F1-S1", VehicleSize.SMALL))
        floor1.add_spot(ParkingSpot("F1-M1", VehicleSize.MEDIUM))
        floor1.add_spot(ParkingSpot("F1-L1", VehicleSize.LARGE))

        floor2 = ParkingFloor(2)
        floor2.add_spot(ParkingSpot("F2-S1", VehicleSize.SMALL))
        floor2.add_spot(ParkingSpot("F2-M1", VehicleSize.MEDIUM))
        floor2.add_spot(ParkingSpot("F2-L1", VehicleSize.LARGE))
        floor2.add_spot(ParkingSpot("F2-L2", VehicleSize.LARGE))

        parking_lot.add_floor(floor1)
        parking_lot.add_floor(floor2)

        floor1.display_availability()
        floor2.display_availability()

        # simulate the vehicle entries
        
        bike = Bike("B-123")
        car = Car("C-145")
        truck = Truck("T-567")
        
        bike_ticket = parking_lot.park_vehicle(bike)
        car_ticket = parking_lot.park_vehicle(car)
        truck_ticket= parking_lot.park_vehicle(truck)

        print("\n Availabily after parking")
        floor1.display_availability()
        floor2.display_availability()

        # simulate the car entry - should go to floor 2
        car2 = Car("C-167")
        car2_ticket = parking_lot.park_vehicle(car2)

        print("\n Availabily after parking")
        floor1.display_availability()
        floor2.display_availability()
        
        # simulate the vehicle entry that fails-  not available
        car3 = Car("C-159")
        car3_ticket = parking_lot.park_vehicle(car3)

        # simulate the vehicle exit and parking fee
        if car_ticket is not None:
            fee = parking_lot.unpark_vehicle(car.get_license_number())
            print(fee)
        
        print("\n AvailabilY")
        floor1.display_availability()
        floor2.display_availability()

if __name__ == "__main__":
    ParkingLotDemo.main()