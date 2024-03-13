# beverage.py
# Caleb Cannon
# beverage.py

class Cup:

    def __init__(self, beverageType, howFull):
        self.beverageType = beverageType
        self.howFull = howFull

    def drink(self):
        if self.howFull > 15:
            self.howFull = self.howFull - 15
            return self.howFull
        else:
            return "You need to refill your drink"

    def dumpOut(self):
        self.howFull = 0
        question = input("Would you like a new drink? ")
        if question[0].lower() == "y":
            newdrink = input("What drink would you like? ")
            self.beverageType = newdrink
            print("Refilling...")
            self.refill()
            return "Your new drink is "+self.beverageType
        else:
            return self.howFull

    def refill(self):
        self.howFull = 100
    
