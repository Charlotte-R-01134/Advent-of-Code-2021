def getPowerConsumptionRate(aList, gamma, epsilon, pos):
    if pos == len(aList[0]):
        return int(gamma, 2) * int(epsilon, 2)

    posList = [item[pos] for item in aList]
    num0 = posList.count("0")
    num1 = posList.count("1")

    if num0 > num1:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

    return getPowerConsumptionRate(aList, gamma, epsilon, pos+1)

aList = [line.rstrip() for line in open('Day 3\day 3.txt')]
gamma = ""
epsilon = ""
print(f"Power Consumption: {getPowerConsumptionRate(aList, gamma, epsilon, 0)}")

def getOxygen(aList, pos, currOxygen):
    if len(aList) == 1:
        return int(currOxygen[0], 2)

    posList = [item[pos] for item in aList]
    num0 = posList.count("0")
    num1 = posList.count("1")
    oxygen = []
    newList = []

    if num0 > num1:
        for item in aList:
            if item[pos] == "0":
                oxygen.append(item)
                newList.append(item)

    if num0 < num1 or num0 == num1:
        for item in aList:
            if item[pos] == "1":
                oxygen.append(item)
                newList.append(item)

    return getOxygen(newList, pos+1, oxygen)

def getCo2(aList, pos, currCo2):
    if len(aList) == 1:
        return int(currCo2[0], 2)

    posList = [item[pos] for item in aList]
    num0 = posList.count("0")
    num1 = posList.count("1")
    co2 = []
    newList = []

    if num0 < num1 or num0 == num1:
        for item in aList:
            if item[pos] == "0":
                co2.append(item)
                newList.append(item)

    if num0 > num1:
        for item in aList:
            if item[pos] == "1":
                co2.append(item)
                newList.append(item)

    return getCo2(newList, pos+1, co2)

oxygen = []
co2 = []
print(f"Life supports: {getOxygen(aList, 0, oxygen) * getCo2(aList, 0, co2)}")