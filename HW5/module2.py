# module2.py
# Caleb Cannon
# A program that utilizes data from the training module to idenitfy mystery pictures.

from graphics import *

def processimg(img):
    numpixels = 0
    red,green,blue = 0,0,0
    width = img.getWidth()
    height = img.getHeight()
    for w in range(width):
            for h in range(height):
                numpixels = numpixels + 1
                r, g, b = img.getPixel(w,h)
                red = red + r
                green = green + g
                blue = blue + b
    avgred = red/numpixels
    avggreen = green/numpixels
    avgblue = blue/numpixels
    return avgred,avggreen,avgblue

def loaddata():
    datalist = []
    avgvals = open('averages.txt', 'r')
    data = avgvals.readline()
    while data != "":
        data = data.split()
        datalist.append(data)
        data = avgvals.readline()
    return datalist
        
def compare(datalist):
    mysteryimg = input('Please enter the name of your mystery file: ')
    win = GraphWin(mysteryimg, 400, 400)
    img = Image(Point(200,200), mysteryimg)
    img.draw(win)
    avgred, avggreen, avgblue = processimg(img)
    result, avgred2, avggreen2, avgblue2 = computation(avgred,avggreen,avgblue,datalist)
    return result,avgred,avggreen,avgblue,avgred2, avggreen2, avgblue2

def computation(avgred,avggreen,avgblue,datalist):
    avgr1, avgr2, avgr3, avgr4, avgr5, avgr6 = figurered(avgred,datalist)
    avgg1, avgg2, avgg3, avgg4, avgg5, avgg6 = figuregreen(avggreen, datalist)
    avgb1, avgb2, avgb3, avgb4, avgb5, avgb6, = figureblue(avgblue, datalist)
    p1 = avgr1 + avgg1 + avgb1
    p2 = avgr2 + avgg2 + avgb2
    p3 = avgr3 + avgg3 + avgb3
    p4 = avgr4 + avgg4 + avgb4
    p5 = avgr5 + avgg5 + avgb5
    p6 = avgr6 + avgg6 + avgb6
    result, avgred2, avggreen2, avgblue2 = closestpicture(p1,p2,p3,p4,p5,p6,datalist)
    return result,avgred2, avggreen2, avgblue2

def closestpicture(p1,p2,p3,p4,p5,p6,datalist):
    sortlist = [p1,p2,p3,p4,p5,p6]
    mostlikely = min(sortlist)
    if mostlikely == p1:
        return datalist[0][0], datalist[0][1], datalist[0][2], datalist[0][3]
    elif mostlikely == p2:
        return datalist[1][0], datalist[1][1], datalist[1][2], datalist[1][3]
    elif mostlikely == p3:
        return datalist[2][0], datalist[2][1], datalist[2][2], datalist[2][3]
    elif mostlikely == p4:
        return datalist[3][0], datalist[3][1], datalist[3][2], datalist[3][3]
    elif mostlikely == p5:
        return datalist[4][0], datalist[4][1], datalist[4][2], datalist[4][3]
    else:
        return datalist[5][0], datalist[5][1], datalist[5][2], datalist[5][3]

def figurered(avgred,datalist):
    d1 = abs(float(datalist[0][1]) - avgred) / avgred
    d2 = abs(float(datalist[1][1]) - avgred) / avgred
    d3 = abs(float(datalist[2][1]) - avgred) / avgred
    d4 = abs(float(datalist[3][1]) - avgred) / avgred
    d5 = abs(float(datalist[4][1]) - avgred) / avgred
    d6 = abs(float(datalist[5][1]) - avgred) / avgred
    return d1,d2,d3,d4,d5,d6

def figuregreen(avggreen, datalist):
    g1 = abs(float(datalist[0][2]) - avggreen) / avggreen
    g2 = abs(float(datalist[1][2]) - avggreen) / avggreen
    g3 = abs(float(datalist[2][2]) - avggreen) / avggreen
    g4 = abs(float(datalist[3][2]) - avggreen) / avggreen
    g5 = abs(float(datalist[4][2]) - avggreen) / avggreen
    g6 = abs(float(datalist[5][2]) - avggreen) / avggreen
    return g1,g2,g3,g4,g5,g6

def figureblue(avgblue, datalist):
    b1 = abs(float(datalist[0][3]) - avgblue) / avgblue
    b2 = abs(float(datalist[1][3]) - avgblue) / avgblue
    b3 = abs(float(datalist[2][3]) - avgblue) / avgblue
    b4 = abs(float(datalist[3][3]) - avgblue) / avgblue
    b5 = abs(float(datalist[4][3]) - avgblue) / avgblue
    b6 = abs(float(datalist[5][3]) - avgblue) / avgblue
    return b1,b2,b3,b4,b5,b6

def displayresult(result,avgred,avggreen,avgblue,avgred2, avggreen2, avgblue2):
    win2 = GraphWin('likeimg', 400, 400)
    likeimg = Image(Point(200,200), result)
    likeimg.draw(win2)
    print()
    print("The closest image is:",result)
    print()
    print("Average rgb values for mystery image: ",avgred, avggreen, avgblue)
    print()
    print("Average rgb values for trained image: ",avgred2, avggreen2, avgblue2)
    
def main():
    datalist = loaddata()
    result,avgred,avggreen,avgblue,avgred2,avggreen2,avgblue2 = compare(datalist)
    displayresult(result,avgred,avggreen,avgblue,avgred2,avggreen2, avgblue2)
main()
