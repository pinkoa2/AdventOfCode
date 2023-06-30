file = open("input.txt", "r")
string = file.read().split("\n")
file.close()

"""
[NW, N, NE, E, SE, S, SW, W]
"""
N = "N"
S = "S"
E = "E"
W = "W"


def getSurroundings(pos):
    result = []
    if (pos[0] - 1, pos[1] - 1) in grid:
        result.append(True)
    else:
        result.append(False)
    if (pos[0], pos[1] - 1) in grid:
        result.append(True)
    else:
        result.append(False)
    if (pos[0] + 1, pos[1] - 1) in grid:
        result.append(True)
    else:
        result.append(False)
    if (pos[0] + 1, pos[1]) in grid:
        result.append(True)
    else:
        result.append(False)
    if (pos[0] + 1, pos[1] + 1) in grid:
        result.append(True)
    else:
        result.append(False)
    if (pos[0], pos[1] + 1) in grid:
        result.append(True)
    else:
        result.append(False)
    if (pos[0] - 1, pos[1] + 1) in grid:
        result.append(True)
    else:
        result.append(False)
    if (pos[0] - 1, pos[1]) in grid:
        result.append(True)
    else:
        result.append(False)
    return result


def printGrid():
    result = 0
    minX = 1000
    maxX = 0
    minY = 1000
    maxY = 0
    for key in grid:
        minX = min(minX, key[0])
        maxX = max(maxX, key[0])
        minY = min(minY, key[1])
        maxY = max(maxY, key[1])
    for y in range(minY, maxY + 1):
        for x in range(minX, maxX + 1):
            if (x, y) in grid:
                print("#", end="")
                continue
            result += 1
            print(".", end="")
        print()
    return result


class Elf:
    def __init__(self, pos):
        self.pos = pos
        self.directions = [N, S, W, E]
        self.choose = None
        self.newPos = None

    def checkSurroundings(self):
        surroundings = getSurroundings(self.pos)
        if True not in surroundings:
            d = self.directions.pop(0)
            self.directions.append(d)
            return
        pos = self.pos
        for direction in self.directions:
            if direction == N:
                if True not in surroundings[0:3]:
                    self.choose = direction
                    self.newPos = (pos[0], pos[1] - 1)
                    break
            if direction == E:
                if True not in surroundings[2:5]:
                    self.choose = direction
                    self.newPos = (pos[0] + 1, pos[1])
                    break
            if direction == S:
                if True not in surroundings[4:7]:
                    self.choose = direction
                    self.newPos = (pos[0], pos[1] + 1)
                    break
            if direction == W:
                if True not in surroundings[6:] and True != surroundings[0]:
                    self.choose = direction
                    self.newPos = (pos[0] - 1, pos[1])
                    break
        d = self.directions.pop(0)
        self.directions.append(d)

    def move(self):
        if self.newPos == None:
            return False
        grid.add(self.newPos)
        grid.remove(self.pos)
        self.pos = self.newPos
        self.newPos = None
        return True


grid = set()
elves = []
y = 0
for line in string:
    x = 0
    for i in line.strip():
        if i == "#":
            grid.add((x, y))
            elves.append(Elf((x, y)))
        x += 1
    y += 1


def allElvesMakeDecision():
    for elf in elves:
        elf.checkSurroundings()


def checkOverlaps():
    checks = {}
    for elf in elves:
        pos = elf.newPos
        if pos not in checks:
            checks[pos] = 1
        else:
            checks[pos] += 1
    remove = set()
    for key in checks:
        if checks[key] > 1:
            remove.add(key)
    for elf in elves:
        if elf.newPos in remove:
            elf.newPos = None


def moveAllElves():
    shouldStop = True
    for elf in elves:
        if elf.move():
            shouldStop = False
    return shouldStop


i = 1
while True:
    allElvesMakeDecision()
    checkOverlaps()
    if moveAllElves():
        print(i)
        break
    i += 1
