#INPUT

with open("Day 5\day 5.txt") as f:
    data = f.readlines()
ventEnds = []
for line in data:
    pos1, pos2 = line.split("\n")[0].split(" -> ")
    pos1 = pos1.split(",")
    pos2 = pos2.split(",")
    ventEnds.append([[int(pos1[0]), int(pos1[1])], [int(pos2[0]), int(pos2[1])]])
grid = []
for x in range(1000):
    newCol = []
    for y in range(1000):
        newCol.append(0)
    grid.append(newCol)

def addVent(grid, pos1, pos2):
    """Add the vent cells between pos1 and pos2 to the grid."""
    x1 = pos1[0]
    x2 = pos2[0]
    y1 = pos1[1]
    y2 = pos2[1]
    # part 1
    if x1==x2:
        if y1>y2:
            while y1>=y2:
                grid[x1][y1] += 1
                y1 -= 1
        elif y1<y2:
            while y1<=y2:
                grid[x1][y1] += 1
                y1 += 1
    elif y1==y2:
        if x1>x2:
            while x1>=x2:
                grid[x1][y1] += 1
                x1 -= 1
        elif x1<x2:
            while x1<=x2:
                grid[x1][y1] += 1
                x1 += 1
        # part 2
        elif x1>x2 and y1>y2:
            while x1>=x2:
                grid[x1][y1] += 1
                x1 -= 1
                y1 -= 1
        elif x1>x2 and y1<y2:
            while x1>=x2:
                grid[x1][y1] += 1
                x1 -= 1
                y1 += 1
        elif x1<x2 and y1>y2:
            while x1<=x2:
                grid[x1][y1] += 1
                x1 += 1
                y1 -= 1
        elif x1<x2 and y1<y2:
            while x1<=x2:
                grid[x1][y1] += 1
                x1 += 1
                y1 += 1
        return grid

def countOverlaps(grid):
    """Count the overlaping vent cells in the grid."""
    overlaps = 0
    for x in range(len(grid)):
        for cell in grid[x]:
            if cell > 1:
                overlaps += 1
    return overlaps

def solution(grid, ventEnds):
    """Find the solution for Day 5, Part 1 and Part 2."""
    for ends in ventEnds:
        grid = addVent(grid, ends[0], ends[1])
    solution = countOverlaps(grid)
    return solution


print(solution(grid, ventEnds))
