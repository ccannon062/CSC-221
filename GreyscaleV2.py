# SaveGrey.py
# Caleb Cannon
# A program that creates a greyscale image and allows you to save it.

from graphics import *

def main():
    win = GraphWin("Greyscale", 400, 400)
    img = Image(Point(200,200), "greyscale.gif")
    img.draw(win)
    conversion = input("Please enter whether you'd like a greyscale or inverted image: ").lower()
    width = img.getWidth()
    height = img.getHeight()
    if conversion[0] == "g":
        for w in range(width):
            for h in range(height):
                r, g, b = img.getPixel(w,h)
                greyscale = (r + g + b)/3
                img.setPixel(w, h, color_rgb(int(greyscale),int(greyscale),int(greyscale)))
    elif conversion[0] == "i":
        for w in range(width):
            for h in range(height):
                r, g, b = img.getPixel(w,h)
                img.setPixel(w, h, color_rgb(int(255 - r), int(255 - g), int( 255 - b)))
    else:
        print("You did not enter a valid input option")
    fname = input("Please enter your file name to save this image: ")
    img.save(fname)
main()
