from os import curdir


def calculateGammeAndEpsilon(aList):
    gamma = ""
    epsilon = ""
    for str in aList:
        counter = 0
        num = aList[0]
        for char in str:
            cuur = str.count(char)
            if cuur > counter:
                counter = cuur
                num = char
        if num == "0":
            gamma += "0"
            epsilon += "1"
        elif num == "1":
            gamma += "1"
            epsilon += "0"
    return(int(gamma, 2) * int(epsilon, 2))

def splitListIntoPositions(alist):

    pos0 = []
    pos1 = []
    pos2 = []
    pos3 = []
    pos4 = []
    pos5 = []
    pos6 = []
    pos7 = []
    pos8 = []
    pos9 = []
    pos10 = []
    pos11 = []

    for str in alist:
        pos0.append(str[0])
        pos1.append(str[1])
        pos2.append(str[2])
        pos3.append(str[3])
        pos4.append(str[4])
        pos5.append(str[5])
        pos6.append(str[6])
        pos7.append(str[7])
        pos8.append(str[8])
        pos9.append(str[9])
        pos10.append(str[10])
        pos11.append(str[11])

    aList = [pos0, pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11]

    return calculateGammeAndEpsilon(aList)

def main():
    aList = [line.rstrip() for line in open('Day 3\day 3.txt')]
    print(splitListIntoPositions(aList))

main()