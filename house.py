from graphics import *

def main():
    win = GraphWin('Five click house', 400, 400)
    message = Text(Point(200,20),"Click twice to draw the walls")
    message.draw(win)
    p1 = win.getMouse()
    p2 = win.getMouse()
    Rectangle(p1, p2).draw(win)
    message.setText("Click once to draw the roof")
    p3 = win.getMouse()
    y_1 = p1.getY()
    y_2 = p2.getY()
    height = abs(y_1 - y_2)
    y1 = y_1 + height
    x1 = p1.getX()
    Polygon(Point(x1, y1), Point(p3), Point(p2)).draw(win)
    
main()
