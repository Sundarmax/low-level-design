
from .fee_strategy import FeeStrategy
from entities.parking_ticket import ParkingTicket

class FlatRateFeeStrategy(FeeStrategy):

    RATE_PER_HOUR = 10.0

    def calculate_fee(self, parking_ticket : ParkingTicket):
        duration = parking_ticket.get_exit_time() - parking_ticket.get_entry_time()
        hours = (duration // (1000 * 60 * 60)) + 2
        return hours * self.RATE_PER_HOUR
