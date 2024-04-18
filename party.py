# party.py
# Caleb Cannon
# Calls room of cups

from roomofcups import *
from beverage import *

party = RoomOfCups()

cups = party.addcups(5)


party.cups[0].drink()

