file = open('input.txt', 'r')
lines = file.read().split('\n')
file.close()

grid = {}

def DrawGrid():
    minimumX = 100000
    minimumY = 100000
    maximumX = 0
    maximumY = 0
    for pos in grid:
        minimumX = min(minimumX, pos[0])
        maximumX = max(maximumX, pos[0])
        minimumY = min(minimumY, pos[1])
        maximumY = max(maximumY, pos[1])
    result = 0
    for y in range(0, maximumY+1):
        for x in range(minimumX, maximumX+1):
            if( (x, y) in grid):
                if(grid[(x, y)] == 0):
                    result += 1
                    # print('o', end = '')
                else:
                    pass
                    # print('#', end='')
            else:
                pass
                # print('.', end='')
        # print()
    print(result+1)
    return maximumY

def drawLine(pos1, pos2):
    if(pos1[0] == pos2[0]):
        for i in range( min(pos1[1], pos2[1]), max(pos1[1], pos2[1])+1):
            grid[(pos1[0], i)] = 1
    if(pos1[1] == pos2[1]):
        for i in range( min(pos1[0], pos2[0]), max(pos1[0], pos2[0])+1):
            grid[(i, pos1[1])] = 1

lines.pop(-1)
for line in lines:
    points = line.split(' -> ')
    normalizedPoints = []
    for point in points:
        posX = int(point.split(',')[0])
        posY = int(point.split(',')[1])
        normalizedPoints.append((posX, posY))
    for i in range(len(normalizedPoints)-1):
        drawLine(normalizedPoints[i], normalizedPoints[i+1])
maxY = DrawGrid()
infinity = 100000
drawLine((-1*infinity, maxY+2), (infinity, maxY+2))

def move(pos):
    posX = pos[0]
    posY = pos[1]
    
    if( (posX, posY + 1) not in grid):
        return (posX, posY+1)
    if( (posX-1, posY+1) not in grid):
        return (posX-1, posY)
    if( (posX+1, posY+1) not in grid):
        return (posX+1, posY)
    return pos

def placeSand(pos):
    moves = 0
    newPos = pos
    oldPos = -1
    while(newPos != oldPos):
        oldPos = newPos
        newPos = move(newPos)
        if(newPos == (500, 0)):
            return False
        moves += 1
        # if(moves >= maxNumberOfMoves):
        #     return False
    grid[newPos] = 0
    return True

starting = (500, 0)
while(placeSand(starting)):
    # Running
        starting = (500, 0)


DrawGrid()

