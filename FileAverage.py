# FileAverage.py
# Caleb Cannon
# This program will take in the contents of a file an determine the total number of words and average word length


def main():
    filename = input("Please enter the name of your file: ")
    infile = open(filename, "r")
    data = infile.read()
    words = data.split()

    wordcount = len(words)

    avglength = len(data) / wordcount


    print("The wordcount is:",wordcount)
    print("The average length is:",round(avglength,2))
    
main()
