fileName = 'input.txt'


class Blizzard:

    def __init__(self, fileName):
        file = open(fileName, 'r')
        self.grid = {}
        self.parse(file)
        file.close()

    def parse(self, file):
        rows = file.read().split('\n')
        rows.pop(-1)
        for y in range(len(rows)):
            for x in range(len(rows[y])):
                symbol = rows[y][x]
                if (symbol not in ['>', '<', 'v', '^', '#']):
                    continue
                self.grid[(x, y)] = [symbol]
        self.minX = 0
        self.minY = 0
        self.maxX = x+1
        self.maxY = y+1

    def __str__(self):
        string = ''
        for y in range(self.minY, self.maxY):
            for x in range(self.minX, self.maxX):
                if ((x, y) not in self.grid):
                    string += '.'
                    continue
                length = len(self.grid[(x, y)])
                if (length == 1):
                    value = self.grid[(x, y)][0]
                else:
                    value = str(length)
                string += value
            string += '\n'
        return string

    def moveSymbol(self, pos, symbol):
        x = pos[0]
        y = pos[1]
        if (symbol == '<'):
            if (x == self.minX+1):
                return (self.maxX-2, y)
            return (x - 1, y)
        if (symbol == '>'):
            if (x == self.maxX-2):
                return (self.minX+1, y)
            return (x+1, y)
        if (symbol == 'v'):
            if (y == self.maxY-2):
                return (x, self.minY+1)
            return (x, y+1)
        if (symbol == '^'):
            if (y == self.minY+1):
                return (x, self.maxY-2)
            return (x, y-1)
        return (x, y)

    def move(self):
        newGrid = {}
        for y in range(self.minY, self.maxY):
            for x in range(self.minX, self.maxX):
                if ((x, y) not in self.grid):
                    continue
                for symbol in self.grid[(x, y)]:
                    nextPos = self.moveSymbol((x, y), symbol)
                    if (nextPos not in newGrid):
                        newGrid[nextPos] = [symbol]
                    else:
                        newGrid[nextPos].append(symbol)
        self.grid = newGrid

    def getBlizzardPos(self):
        positions = set()
        for y in range(self.minY, self.maxY):
            for x in range(self.minX, self.maxX):
                pos = (x, y)
                if (pos not in self.grid):
                    continue
                for symbol in self.grid[pos]:
                    if (symbol in ['>', '<', 'v', '^', '#']):
                        positions.add(pos)
        return positions


def getNextPositions(blizzard, pos):
    x = pos[0]
    y = pos[1]
    setOfPositions = set([
        (x, y),
        (x-1, y),
        (x+1, y),
        (x, y+1),
        (x, y-1)
    ])
    # return setOfPositions
    return removeOutOfBound(blizzard, setOfPositions)


def removeOutOfBound(blizzard, positions):
    positionsToRemove = set()
    maxX = blizzard.maxX
    maxY = blizzard.maxY
    for pos in positions:
        x = pos[0]
        y = pos[1]
        if (x < 0 or x > maxX):
            positionsToRemove.add(pos)
        if (y < 0 or y > maxY):
            positionsToRemove.add(pos)
    return positions.difference(positionsToRemove)


blizzard = Blizzard(fileName)
STARTING = (1, 0)
ENDING = (blizzard.maxX-2, blizzard.maxY-1)

setOfPeople = set([STARTING])
roundNumber = 0
while (ENDING not in setOfPeople):
    nextSetOfPeople = set()
    for person in setOfPeople:
        surround = getNextPositions(blizzard, person)
        nextSetOfPeople = nextSetOfPeople.union(surround)
    nextSetOfPeople = nextSetOfPeople.difference(blizzard.getBlizzardPos())
    roundNumber += 1
    setOfPeople = nextSetOfPeople
    print(roundNumber)
    blizzard.move()

print(roundNumber-1)
print(len(setOfPeople))
removeOutOfBounds = removeOutOfBound(blizzard, setOfPeople)
