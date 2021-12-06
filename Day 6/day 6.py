def getFish():
    listOfFish = []
    with open('Day 6\day 6.txt')as f:
        data = f.readline()
        listOfFish = [int(x) for x in data.split(',')]
    return listOfFish

def runSimulation():
    listOfFish = getFish()
    for day in range(80):
        for i in range(len(listOfFish)):
            if listOfFish[i] == 0:
                listOfFish[i] = 6
                listOfFish.append(8)
            else:
                listOfFish[i] -= 1
    return len(listOfFish)

print(runSimulation())

