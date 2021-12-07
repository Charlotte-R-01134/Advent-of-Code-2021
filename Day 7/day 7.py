import math

def getCrabPos():
    listOfCrabPos = []
    with open('Day 7\day 7.txt')as f:
        data = f.readline()
        listOfCrabPos = [int(x) for x in data.split(',')]
    return listOfCrabPos

def findMinFuelConsumption(listOfCrabPos):
    # sum of absolute value - median of values
    listOfCrabPos.sort()
    median = listOfCrabPos[math.floor(len(listOfCrabPos)/2)]
    minFuelConsumption = 0
    for crabPos in listOfCrabPos:
        minFuelConsumption += abs(crabPos - median)
    return minFuelConsumption

listOfCrabPos = getCrabPos()
print(findMinFuelConsumption(listOfCrabPos))

def getTriangularNumber(n):
    return n*(n+1)//2

def findMinFuelConsumptionWithExponentialGrowth(listOfCrabPos):
    results = []
    for point in range(0, max(listOfCrabPos)):
        fuel = sum([getTriangularNumber(abs(crab-point)) for crab in listOfCrabPos])
        results.append(fuel)
    return min(results)

listOfCrabPos = getCrabPos()
print(findMinFuelConsumptionWithExponentialGrowth(listOfCrabPos))

