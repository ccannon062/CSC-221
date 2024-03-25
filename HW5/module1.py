# module1.py
# Caleb Cannon
# A module that loads images in, traverses the images, and stores the average RGB values per image

from graphics import *

def avgrgb(img):
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
    
def loadimg(img):
    win = GraphWin(img, 400, 400)
    img = Image(Point(200,200), img)
    img.draw(win)
    return img

def loadimages():
    img1 = loadimg('DaVinci1.gif')
    img2 = loadimg('Davinci2.gif')
    img3 = loadimg('Davinci3.gif')
    img4 = loadimg('Rembrandt1.gif')
    img5 = loadimg('Rembrandt2.gif')
    img6 = loadimg('Rembrandt3.gif')
    return img1, img2, img3, img4, img5, img6

def export(img1,img2,img3,img4,img5,img6):
    ofile = open('averages.txt', 'w')
    avgred,avggreen,avgblue = avgrgb(img1)
    print('DaVinci1.gif',avgred,avggreen,avgblue, file=ofile)
    avgred,avggreen,avgblue = avgrgb(img2)
    print('DaVinci2.gif',avgred,avggreen,avgblue, file=ofile)
    avgred,avggreen,avgblue = avgrgb(img3)
    print('DaVinci3.gif',avgred,avggreen,avgblue, file=ofile)
    avgred,avggreen,avgblue = avgrgb(img4)
    print('Rembrandt1.gif',avgred,avggreen,avgblue, file=ofile)
    avgred,avggreen,avgblue = avgrgb(img5)
    print('Rembrandt2.gif',avgred,avggreen,avgblue, file=ofile)
    avgred,avggreen,avgblue = avgrgb(img6)
    print('Rembrandt3.gif',avgred,avggreen,avgblue, file=ofile)

def main():
    img1, img2, img3, img4, img5, img6 = loadimages()
    export(img1,img2,img3,img4,img5,img6)
main()
