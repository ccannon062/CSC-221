# Caleb Cannon
# loopingpizza.py
# Compares 3 pizza sizes for a Papa Murphy's Take-and-Bake pizza!

import math

def intro():
    print("Welcome to the looping pizza program!")

def getData():
    diameter = int(input("Please enter the diameter of the pizza size that you are calculating: "))
    price = float(input("Please enter the price of the pizza size: "))
    size_name = input("Please enter the size of your pizza (small, medium, large): ")

    return diameter, price, size_name

def computePricePerSqInch(diameter,price):
    area = math.pi * diameter / 2 ** 2
    per_sqinch = round(price / area, 3)

    return per_sqinch

def main():
    intro()
    for i in range(3):
        d,p,s = getData()
        cost = computePricePerSqInch(d,p)
        print()
        print("Pizza size: ",s)
        print()
        print("Diameter: ",d)
        print()
        print("Price: ",p)
        print()
        print("Price per square inch: ", "$" ,cost)
        print()
main()
