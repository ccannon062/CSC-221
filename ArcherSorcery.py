# ArcherySorcerer.py
# Caleb Cannon
# A game of darts that keeps track of your score over 5 throws.

from graphics import *
from math import *

def calcScore(distancep):
    pointtotal = 0
    if distancep <= 2:
        pointtotal += 9
        print("You scored a 9!")
    elif distancep > 2 and distancep <=4:
        pointtotal += 7
        print("You scored a 7!")
    elif distancep > 4 and distancep <=6:
        pointtotal += 5
        print("You scored a 5!")
    elif distancep > 6 and distancep <=8:
        pointtotal += 3
        print("You scored a 3!")
    elif distancep > 8 and distancep <=10:
        pointtotal += 1
        print("You scored a 1!")
    else:
        pointtotal += 0
        print("You scored a 0!")
    return pointtotal

def calcDistance(click):
    xval = click.getX()
    yval = click.getY()
    return sqrt(abs(0 - xval)**2+abs(0-yval)**2)

def main():
    # Drawing shapes
    win = GraphWin('Sorcerer Archery',400,400)
    win.setCoords(-11,-11,11,11)
    circ1 = Circle(Point(0,0), 10)
    circ1.draw(win)
    circ1.setFill('white')
    circ2 = Circle(Point(0,0), 8)
    circ2.draw(win)
    circ2.setFill('black')
    circ3 = Circle(Point(0,0), 6)
    circ3.draw(win)
    circ3.setFill('blue')
    circ4 = Circle(Point(0,0), 4)
    circ4.draw(win)
    circ4.setFill('red')
    circ5 = Circle(Point(0,0), 2)
    circ5.draw(win)
    circ5.setFill('yellow')

    
    # Calculating points
    pointtotal = 0
    click1 = win.getMouse()
    distancep1 = calcDistance(click1)
    pointtotal += calcScore(distancep1)
    print("Your new total is:",pointtotal)
    click2 = win.getMouse()
    distancep2 = calcDistance(click2)
    pointtotal += calcScore(distancep2)
    print("Your new total is:",pointtotal)
    click3 = win.getMouse()
    distancep3 = calcDistance(click3)
    pointtotal += calcScore(distancep3)
    print("Your new total is:",pointtotal)
    click4 = win.getMouse()
    distancep4 = calcDistance(click4)
    pointtotal += calcScore(distancep4)
    print("Your new total is:",pointtotal)
    click5 = win.getMouse()
    distancep5 = calcDistance(click5)
    pointtotal += calcScore(distancep5)
    print("Your new total is:",pointtotal)
main()
