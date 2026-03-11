

from inventory.stock_inventory import Inventory
from data.item import Item
from enums.coin import Coin
from states.vending_machine_state import *

class VendingMachine:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(VendingMachine, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized') or not self._initialized:
            self.inventory = Inventory()
            self.current_state = IdleState(self)
            self.balance = 0
            self.selected_item_code = None
            self._initialized = True

    def get_instance(cls):
        return cls()
    
    def add_item(self,name : str,code : str,price : int,quantity : int):
        itm = Item(name,price,code)
        self.inventory.add_item(code, itm, quantity)
        return itm
    
    def select_item(self, code : str):
        self.current_state.select_item(code)

    def insert_coin(self,coin : Coin):
        self.current_state.insert_coin(coin)

    def dispense(self):
        self.current_state.dispense()

    def dispense_item(self):
        itm = self.inventory.get_item(self.selected_item_code)
        if itm.get_price() <= self.balance :
            self.inventory.reduce_stock(self.selected_item_code) 
            self.balance -=itm.get_price()
            print(f"Dispensed : {itm.get_name()}")
            if self.balance > 0:
                print(f"Returning change {self.balance}")
        self.reset()
        self.set_state(IdleState(self))

    def reset(self):
        self.balance = 0
        self.selected_item_code = None

    def add_balance(self, value  : int) -> None:
        self.balance += value
    
    # Setter methods

    def set_selected_item_code(self, code : str):
        self.selected_item_code = code

    def set_state(self, state : VendingMachineState) -> None:
        self.current_state = state
    
    # Getter methods
    def get_inventory(self):
        return self.inventory
    
    def get_balance(self):
        return self.balance
    
    def get_selected_item(self):
        return self.inventory.get_item(self.selected_item_code)

