# SumSquaresFile.py
# Caleb Cannon
# A program that takes in a file name, puts numbers in a list, squares them, and also adds them

from math import *

def toNumbers(data):
    newlist = []
    data = data[0:-1]
    for items in data:
        values = int(items)
        newlist.append(values)
    return newlist

def squareEach(newlist):
    for items in range(len(newlist)):
        newlist[items]=newlist[items]**2
    return newlist

def sumList(newlist):
    total = 0
    for items in range(0, len(newlist)):
        total = total + newlist[items]
    return total

def printList(listitems):
    for items in listitems:
        print(items)

def main():
    fname = input("Please enter the file name: ")
    infile = open(fname, "r")
    data = infile.read()
    newlist = toNumbers(data)
    printList(newlist)
    print()
    sums = sumList(newlist)
    print(sums)
    print()
    squares = squareEach(newlist)
    printList(squares)
    infile.close()
main()
