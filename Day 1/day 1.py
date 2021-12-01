def findMeasurements(aList):
    count = 0
    for i in range(len(aList)-1):
        if aList[i] < aList[i+1] + 1:
            count += 1
    return count

def main():
    aList = [int(x) for x in open('Day 1\day 1.txt').read().splitlines()]
    print(findMeasurements(aList))

main()