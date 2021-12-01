def findDepthMeasurementIncrease(aList):
    count = 0
    for i in range(len(aList)-1):
        if aList[i] < aList[i+1]:
            count += 1
    return count

def findSumOfMeasurementsIncrease(aList):
    sumList = []
    for i in range(len(aList)-2):
        total = aList[i] + aList[i+1] + aList[i+2]
        sumList.append(total)
    return findDepthMeasurementIncrease(sumList)


def main():
    aList = [int(x) for x in open('Day 1\day 1.txt').read().splitlines()]
    print(findDepthMeasurementIncrease(aList))
    print(findSumOfMeasurementsIncrease(aList))

main()