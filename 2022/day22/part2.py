file = open('input.txt', 'r')
parsed = file.read().split('\n\n')
file.close()

'''
  12
  3
 45
 6
'''
clockwise = {
    'UP': "RIGHT",
    'RIGHT': 'DOWN',
    'DOWN': 'LEFT',
    'LEFT': 'UP'
}
counterClockwise = {
    'UP': 'LEFT',
    'LEFT': 'DOWN',
    'DOWN': 'RIGHT',
    'RIGHT': 'UP'
}

def parseInstructions(instructions):
    numbers = '1234567890'
    line = instructions.strip()
    instructions = []
    direction = 'R'
    number = 0
    for i in line:
        if(i in numbers):
            number = number * 10
            number = number + int(i)
        else:
            instructions.append( (direction, number) )
            direction = i
            number = 0
    instructions.append( (direction, number))
    return instructions

def printGrid(num, grid):
    for y in range(0, 50):
        for x in range(0,50):
            print(grid[(num, x, y)], end ='')
        print()

def parseGrid(string):
    grid = {}

    # Grid 1
    lines = string.split('\n')
    for x in range(0, 50):
        for y in range(0, 50):
            grid[ (1, x, y) ] = lines[y][x+50]

    # Grid 2
    for x in range(0, 50):
        for y in range(0, 50):
            grid[ (2, x, y) ] = lines[y][x+100]

    # Grid 3
    for x in range(0, 50):
        for y in range(0, 50):
            grid[ (3, x, y) ] = lines[y+50][x+50]

    # Grid 4
    for x in range(0, 50):
        for y in range(0, 50):
            grid[ (4, x, y) ] = lines[y+100][x]

    # Grid 5
    for x in range(0, 50):
        for y in range(0, 50):
            grid[ (5, x, y) ] = lines[y+100][x+50]

    # Grid 6
    for x in range(0, 50):
        for y in range(0, 50):
            grid[ (6, x, y) ] = lines[y+150][x]

    return grid

def travelDirection(pos, direction, distance):
     

def changeBoards(pos, direction, distance):
    boardNum = pos[0]
    if(boardNum == 1 and direction == 'RIGHT'):
        newBoard = 2
        newPos = (newBoard, 0, pos[2])
        newDirection = 'RIGHT'
        return travelPosX(newPos, distance)
    
def travelPosX(pos, distance):
    newPos = ( pos[0], pos[1] + 1, pos[2] )
    if(grid[newPos] == '#'):
        return pos
    if(distance <= 0):
        return newPos
    if(newPos[0] >= 50):
        return changeBoards(newPos, 'RIGHT', distance-1)
    return travelPosX(newPos, distance-1) 

instructions = parseInstructions(parsed[1])
grid = parseGrid(parsed[0])
printGrid(6, grid)










# if(endPos == 'RIGHT'):
#     endPos = 0
# elif(endPos == 'DOWN'):
#     endPos = 1
# elif(endPos == 'LEFT'):
#     endPos = 2
# else:
#     endPos = '3'

# print(1000*endY+4*endX+endPos)

# for row in range(minY, maxY+1):
#     for col in range(minX, maxX+1):
#         pos = (col, row)
#         if(pos not in grid):
#             print(' ', end='')
#         else:
#             print(grid[pos], end = '')
#     print()

