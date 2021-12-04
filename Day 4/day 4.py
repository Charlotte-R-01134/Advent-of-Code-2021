
def getInput():
    return [line.rstrip() for line in open("Day 4\day 4.txt").readline().rstrip().split(",")]

def getCards():
    with open("Day 4\day 4.txt") as f:
        lines = f.readlines()[2:]
        Matrix = []
        table = []
        for line in lines:
            if line == "\n":
                Matrix.append(table)
                table = []
                continue
            numbers = []
            row = line.rstrip().split(" ")
            for num in row:
                if num == "":
                    row.pop(row.index(num))
            numbers.append(row)
            table.append(numbers)
        Matrix.append(table)
    return Matrix

def markSelected(Matrix, input):
    for card in Matrix:
        for table in card:
            for row in table:
                for num in row:
                    if num == input:
                        Matrix[Matrix.index(card)][card.index(table)][table.index(row)][row.index(num)] = ""
    return Matrix

def calculateScore(card, input):
    score = 0
    for table in card:
        for row in table:
            for num in row:
                if num != "":
                    score += int(num)
    print(score*int(input))

def checkIfBingo(Matrix, input):
    for card in Matrix:
        for table in card:
            for row in table:
                x = row.count("")
                if x == len(row):
                    print("BINGO!")
                    calculateScore(card, input)
                    return True

def playgame():
    Matrix = getCards()
    input = getInput()
    for i in input:
        Matrix = markSelected(Matrix, i)
        if checkIfBingo(Matrix, i):
            break

playgame()


