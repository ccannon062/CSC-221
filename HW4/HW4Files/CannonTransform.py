# CannonFernandezHW4.py
# By Caleb Cannon and Paul Fernandez
# A program that takes Xml and converts it into an HTML document.

def setup():
    infile = open("WTExcerpt.xml","r",encoding="UTF8")
    outfile = open("WTExcerpt.html","w",encoding="UTF8")

    print("<html>\n<head>\n<title>The Winter's Tale</title>",file=outfile)
    print("<meta http-equiv='content-type' content='text/html;charset=utf-8' />",file=outfile)
    print("<link rel='stylesheet' type='text/css' href='Shakespeare.css'>",file=outfile)
    print("</head>\n<body>",file=outfile)

    text = infile.readline()

    while text!="":
        if text[0:7] == "<title>":
            print("<h1>", end="", file=outfile)
            theWords = text.split()
            print(theWords[1], end=" ", file=outfile)
            print(theWords[2], end=" ", file=outfile)
            print(theWords[3], end="", file=outfile)
            print("</h1>", file=outfile)
        elif text == "<head>\n":
            print("<h3>", end="", file=outfile)
            while text != "</head>\n":
                text=infile.readline()
                if text[1] == "w":
                    theWords = text.split()
                    print(theWords[1], end=" ", file=outfile)
            print("</h3>", file=outfile)
        elif text == "<stage>\n":
            print("<h4>", end="", file=outfile)
            while text != "</stage>\n":
                text = infile.readline()
                if text[1] == "w":
                    theWords = text.split()
                    print(theWords[1], end=" ", file=outfile)
            print("<h4>", file=outfile)        
        elif text == "<speaker>\n":
            print("<h2>",end="",file=outfile)
            text = infile.readline()
            theWords = text.split()
            print(theWords[1],end="",file=outfile)
            print("</h2>",file=outfile)
        elif text[0:4] == "<fw>":
            print("<h3>", end="", file=outfile)
            theWords = text.split()
            print(theWords[1], end="", file=outfile)
            print(theWords[2], end="", file=outfile)
            print(theWords[3], end="", file=outfile)
            print(theWords[4], end="", file=outfile)
            print("</h3>", file=outfile)
        else:
            if text[0:3] == "<w>":
                if text[4].isupper() == True:
                    print("</p>\n<br>\n<p>", file=outfile)
                print(text[3:-5], file=outfile)
            if text[0:4] == "<pc>":
                print(text[4], file=outfile)
        text = infile.readline()
    print("</body>\n</html>",file=outfile)
def main():
    setup()


main()
