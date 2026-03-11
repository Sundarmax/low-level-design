
from facade.vending_machine import VendingMachine
from enums.coin import Coin

vending_machine = VendingMachine()

# add item to inventory
vending_machine.add_item("soda","SDA",1,10)
vending_machine.add_item("cola","CLA",2,10)

# select - Add extra amounts
vending_machine.select_item("SDA")
# vending_machine.select_item("CLA")
vending_machine.insert_coin(Coin.FIVE_RUPEE)
vending_machine.dispense()


# select - Add exact amount.
vending_machine.select_item("CLA")
vending_machine.insert_coin(Coin.TWO_RUPEE)
vending_machine.dispense()