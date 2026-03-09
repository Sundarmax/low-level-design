
from abc import ABC,abstractmethod
from enums.coin import Coin

class VendingMachineState(ABC):

    def __init__(self, machine):
        super().__init__(machine)

    @abstractmethod
    def insert_coin(self, coin : Coin) -> None:
        pass
    
    @abstractmethod
    def select_item(self, code : str) -> None:
        pass

    @abstractmethod
    def dispense(self) -> None:
        pass

    @abstractmethod
    def refund(self) -> None:
        pass


class IdleState(VendingMachineState):

    def __init__(self, machine):
        super().__init__(machine)

    def insert_coin(self, coin):
        print("Select the item first")
    
    def select_item(self, code):
        if not self.machine.get_inventory().is_available(code):
            print("Item not available.")
            return
        self.machine.set_selected_item_code(code)
        self.machine.set_state(SelectedItemState(self.machine))

    def dispense(self):
        print("No item selected")
    
    def refund(self):
        print("No money to refund")


class SelectedItemState(VendingMachineState):

    def __init__(self, machine):
        super().__init__(machine)

    def insert_coin(self, coin : Coin):
        self.machine.add_balance(coin.get_value())
        print(f"coin inserted : {coin.get_value()}")
        price = self.machine.get_selected_item().get_price()
        if self.machine.get_balance() >=price:
            print("Sufficient money received")
            self.machine.set_state(HasMoneyState(self.machine))

    def select_item(self, code):
        print("Item alredy selected")

    def dispense(self):
        print("Please insert the coin first")
    
    def refund(self):
        pass

class HasMoneyState(VendingMachineState):
    
    def __init__(self, machine):
        super().__init__(machine)
    
    def insert_coin(self, coin : Coin):
        print("Already Received the full amount. !")

    def select_item(self, code):
        print("Item alredy selected")

    def dispense(self):
        self.machine.set_state(DispenseState(self.machine))
        self.machine.dispense_item()
    
    def refund(self):
        pass

class DispenseState(VendingMachineState):
    
    def __init__(self, machine):
        super().__init__(machine)
    
    def insert_coin(self, coin : Coin):
        print("Currently dispensing . ! Please wait. !")

    def select_item(self, code):
        print("Currently dispensing . ! Please wait. !")

    def dispense(self):
        pass
    
    def refund(self):
        print("Currently dispensing . ! Not allowed. !")