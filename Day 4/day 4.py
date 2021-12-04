
def getInput():
    """
    gets inputs from start of txt file
    """
    return [line.rstrip() for line in open("Day 4\day 4.txt").readline().rstrip().split(",")]

def getCards():
    """
    Sorts each card into a matrix
    """
    with open("Day 4\day 4.txt") as f:
        lines = f.readlines()[2:]
        Matrix = []
        card = []
        for line in lines:
            if line == "\n":
                continue
            row = line.rstrip().split(" ")
            for num in row:
                if num == "":
                    row.pop(row.index(num))
            card.append(row)
            if len(card) == 5:
                    Matrix.append(card)
                    card = []
                    continue
    return Matrix

def markSelected(Matrix, input):
    """
    Search for input in Matrix
    """
    for card in Matrix:
            for row in card:
                for num in row:
                    if num == input:
                        Matrix[Matrix.index(card)][card.index(row)][row.index(num)] = ""
    return Matrix

def calculateScore(card, input):
    score = 0
    for row in card:
        for num in row:
            if num != "":
                score += int(num)
    print(score*int(input))

def checkIfBingo(Matrix, input):
    """
    Searches row and column for full empty row or column
    """
    for card in Matrix:
        for row in range(5):
            for col in range(5):
                if card[row][col] == "":
                    x = card[row].count("")
                    if x == len(card[row]):
                        print("Bingo!")
                        calculateScore(card, input)
                        return True
            if card[col][row] == "":
                x = card[col].count("")
                if x == len(card[col]):
                    print("Bingo!")
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


