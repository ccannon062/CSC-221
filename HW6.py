# interest.py
# Caleb Cannon
# This program will take your initial principal, calculate your interest over a period of time, and return the final value with a graph.

from graphics import *

def drawgraph(amounts):
    win = GraphWin('Interest growth',400,400)
    win.setCoords(0,0,100,100)
    proportion = []
    for i in amounts:
        proportion.append(round(i/1000,2))
    drawy(win)
    drawx(win)
    drawpoints(win,proportion)

def drawy(win):
    tenk = Text(Point(3,10),'10K')
    tenk.draw(win)
    twentk = Text(Point(3,20),'20K')
    twentk.draw(win)
    thirtyk = Text(Point(3,30),'30K')
    thirtyk.draw(win)
    fortyk = Text(Point(3,40),'40K')
    fortyk.draw(win)
    fiftyk = Text(Point(3,50),'50K')
    fiftyk.draw(win)
    sixtyk = Text(Point(3,60),'60K')
    sixtyk.draw(win)
    seventyk = Text(Point(3,70),'70K')
    seventyk.draw(win)
    eightyk = Text(Point(3,80),'80K')
    eightyk.draw(win)
    ninetyk = Text(Point(3,90),'90K')
    ninetyk.draw(win)

def drawx(win):
    year10 = Text(Point(10, 3), '10Y')
    year10.draw(win)
    year20 = Text(Point(20, 3), '20Y')
    year20.draw(win)
    year30 = Text(Point(30, 3), '30Y')
    year30.draw(win)
    year40 = Text(Point(40, 3), '40Y')
    year40.draw(win)
    year50 = Text(Point(50, 3), '50Y')
    year50.draw(win)
    year60 = Text(Point(60, 3), '60Y')
    year60.draw(win)
    year70 = Text(Point(70, 3), '70Y')
    year70.draw(win)
    year80 = Text(Point(80, 3), '80Y')
    year80.draw(win)
    year90 = Text(Point(90, 3), '90Y')
    year90.draw(win)

def drawpoints(win, proportion):
    interest10 = Point(10,int(proportion[10]+3))
    interest10.draw(win)
    interest20 = Point(20,int(proportion[20]+3))
    interest20.draw(win)
    interest30 = Point(30,int(proportion[30]+3))
    interest30.draw(win)
    interest40 = Point(40,int(proportion[40]+3))
    interest40.draw(win)
    interest50 = Point(50,int(proportion[50]+3))
    interest50.draw(win)
    interest60 = Point(60,int(proportion[60]+3))
    interest60.draw(win)
    interest70 = Point(70,int(proportion[70]+3))
    interest70.draw(win)
    interest80 = Point(80,int(proportion[80]+3))
    interest80.draw(win)
    interest90 = Point(90,int(proportion[100-1]))
    interest90.draw(win)
    drawlines(interest10,interest20,interest30,interest40,interest50,interest60,interest70,interest80,interest90,win)

def drawlines(interest10,interest20,interest30,interest40,interest50,interest60,interest70,interest80,interest90,win):
    ylist = []
    pointslist = [interest10,interest20,interest30,interest40,interest50,interest60,interest70,interest80,interest90]
    for points in pointslist:
        ylist.append(points.getY())
    point1 = Line(Point(10,ylist[0]), Point(20,ylist[1]))
    point1.draw(win)
    point2 = Line(Point(20,ylist[1]), Point(30,ylist[2]))
    point2.draw(win)
    point3 = Line(Point(30,ylist[2]), Point(40,ylist[3]))
    point3.draw(win)
    point4 = Line(Point(40,ylist[3]), Point(50,ylist[4]))
    point4.draw(win)
    point5 = Line(Point(50,ylist[4]), Point(60,ylist[5]))
    point5.draw(win)
    point6 = Line(Point(60,ylist[5]), Point(70,ylist[6]))
    point6.draw(win)
    point7 = Line(Point(70,ylist[6]), Point(80,ylist[7]))
    point7.draw(win)
    point8 = Line(Point(80,ylist[7]), Point(90,ylist[8]))
    point8.draw(win)
    

def intro():
    print("Hello, welcome to the interest calculator!")
    print("In order to show you the true power of compound interest, this program will track your interest over one hundred years and display it on a graph!")
    print()

def compute():
    p = float(input("What is your initial principal amount? (initial deposit requires at least $1,000) "))
    initial = p
    print()
    r = float(input("What is the rate of return on your investment? (3-5%) "))
    print()
    n = int(input("What is the compound frequency of your investment? (Choose: 1, 2, 4, 12, 136) "))
    print()
    r = r / 100

    totallist = []
    for i in range(100):
        a = p * (1 +r/n)**(n*1)
        p = a
        totallist.append(round(p,2))
    
    return totallist, initial

def statement(amounts, initial):
    year = 0
    for i in range(100):
        if i % 10 == 0:
            print("Year",str(year)+":",amounts[i])
        year = year + 1
    print()
    print("Your total balance after one hundred years is: $",amounts[len(amounts)-1])
    print()
    print("The approximate return on your investment is: $",int(amounts[len(amounts)-1]-initial))
    print()

def main():
    intro()
    amounts, initial = compute()
    drawgraph(amounts)
    statement(amounts, initial)
main() 
    
