
def getText():
    infile = open("novel.txt","r")
    allText = infile.read()
    return allText
def nfilter(wList, fList):
    nList = []
    nfList = []
    outfile = open("ignore.txt", "w")
    for word in wList:
        index = wList.index(word)
        if len(word) < 7 or fList[index] > 10:
            print(word, fList[index], file=outfile)
        else:
            nList.append(word)
            nfList.append(fList[index])
    return nList, nfList
def inspectWord(theWord,wList,fList):
        tempWord = theWord.rstrip("\"\'.,`;:-!?")
        tempWord = tempWord.lstrip("\"\'.,`;:-!")
        tempWord = tempWord.lower()
        if tempWord in wList:
              tIndex = wList.index(tempWord)
              fList[tIndex]+=1
        else:
              wList.append(tempWord)
              fList.append(1)
def printParallelLists(wList,fList):
    for i in range(len(wList)):
        print(wList[i],fList[i])
def main():
    wList = []
    fList = []
    myText = getText()
    myWords = myText.split(" ")
    for word in myWords:
        inspectWord(word,wList,fList)
    nList, nfList = nfilter(wList, fList)
    print(myText)
    printParallelLists(nList,nfList)
    
main()
