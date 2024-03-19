import re

def solvepart1():
    scratchCards = fileRead("input.txt")
    sum = 0
    for card in scratchCards:
        line = card.split(":")[1].split("|")
        winningNums = re.sub("  ", " ",line[0].strip()).split(" ")
        haveNums = re.sub("  ", " ",line[1].strip()).split(" ")
        numwins = 0
        for haveNum in haveNums:
            if (haveNum in winningNums):
                numwins = numwins + 1
        points = 0
        if (numwins > 0):    
            points = 1 * pow(2,numwins-1)
        sum = sum + points;
    print(sum)

def solvepart2():
    scratchCards = fileRead("input.txt")
    winningCardsDict = {}
    for i in range(len(scratchCards)):
        winningCardsDict[i] = 1
    for i, card in enumerate(scratchCards):
        line = card.split(":")[1].split("|")
        winningNums = re.sub("  ", " ",line[0].strip()).split(" ")
        haveNums = re.sub("  ", " ",line[1].strip()).split(" ")
        numwins = 0
        for haveNum in haveNums:
            if (haveNum in winningNums):
                numwins = numwins + 1
        for j in range(numwins):
            winningCardsDict[i+j+1] = winningCardsDict[i+j+1] + winningCardsDict[i]
    totalCards = 0
    for k,v in winningCardsDict.items():
        totalCards = totalCards + v
    print(totalCards)

def fileRead(name):
    data = []
    f = open(name, "r")
    for line in f:
        data.append(line);
    return data

solvepart2()