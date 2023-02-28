fileName = 'simple.txt'


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
                symbol = rows[x][y]
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
                return (self.maxX-1, y)
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
                return (x, self.maxY-1)
            return (x, y-1)
        return (x, y)

    def move(self):
        print(self.maxY)
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


blizzard = Blizzard(fileName)
print(str(blizzard))
blizzard.move()
print(str(blizzard))
blizzard.move()
print(str(blizzard))
