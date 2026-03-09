
from data.item import Item


class Inventory:

    def __init__(self):
        self.item_map : dict[str, Item] = {}
        self.stock_map : dict[str, int] = {}
    
    def add_item(self,code : str, itm: Item, quantity: int):
        self.item_map[code] = itm
        self.stock_map[code] = quantity
    
    def is_available(self,code: str) -> bool:
        return self.stock_map[code] > 0

    def reduce_stock(self,code: str):
        curr_stock = self.stock_map[code]
        self.stock_map[code] = curr_stock-1

    def get_item(self,code: str) -> Item:
        return self.item_map[code]