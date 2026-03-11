
class Item:
    def __init__(self,name : str,price : int,code : str):
        self.name = name
        self.code = code
        self.price = price
    
    def get_name(self) -> str:
        return self.name

    def get_price(self) -> int:
        return self.price

    def get_item_code(self):
        return self.code