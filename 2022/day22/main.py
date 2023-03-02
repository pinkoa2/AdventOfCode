file = open('input.txt', 'r')
parsed = file.read().split('\n\n')
file.close()

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

def parseGrid(string):
    maxX = 0
    grid = {}
    lines = string.split('\n')
    row = 0
    for line in lines:
        for col in range(len(line)):
            maxX = max(maxX, col)
            letter = line[col]
            if(letter == ' '):
                continue
            grid[ (col, row) ] = letter
        row += 1
    return ( 0, maxX, 0, row, grid)

def travelPosX(pos, distance):
    for _ in range(distance):
        newPos = ( pos[0] + 1, pos[1])
        if(newPos not in grid):
            newPos = ( 0 , pos[1])
            while(newPos not in grid):
                newPos = ( newPos[0] + 1, newPos[1] )
        if(grid[newPos] == '#'):
            return pos
        grid[pos] = '>'
        pos = newPos
    return pos
        
def travelNegX(pos, distance):
    for _ in range(distance):
        newPos = ( pos[0] - 1, pos[1])
        if(newPos not in grid):
            newPos = ( maxX, pos[1])
            while(newPos not in grid):
                newPos = ( newPos[0] - 1, newPos[1] )
        if(grid[newPos] == '#'):
            return pos
        grid[pos] = '<'
        pos = newPos
    return pos

def travelPosY(pos, distance):
    for _ in range(distance):
        newPos = ( pos[0], pos[1] + 1)
        if(newPos not in grid):
            newPos = ( pos[0], 0 )
            while(newPos not in grid):
                newPos = ( newPos[0], newPos[1] + 1 )
        if(grid[newPos] == '#'):
            return pos
        grid[pos] = 'v'
        pos = newPos
    return pos

def travelNegY(pos, distance):
    for _ in range(distance):
        newPos = ( pos[0], pos[1] - 1)
        if(newPos not in grid):
            newPos = ( pos[0], maxY )
            while(newPos not in grid):
                newPos = ( newPos[0], newPos[1] - 1 )
        if(grid[newPos] == '#'):
            return pos
        grid[pos] = '^'
        pos = newPos
    return pos

def traverse(instructions, pos):
    direction = 'UP'
    for instruction in instructions:
        rotation = instruction[0]
        distance = instruction[1]
        if( rotation == 'R' ):
            direction = clockwise[direction]
        elif( rotation == 'L'):
            direction = counterClockwise[direction]
        if(direction == 'UP'):
            pos = travelNegY(pos, distance)
        elif(direction == 'DOWN'):
            pos = travelPosY(pos, distance)
        elif(direction == 'RIGHT'):
            pos = travelPosX(pos, distance)
        elif(direction == 'LEFT'):
            pos = travelNegX(pos, distance)
        print(direction, pos)
    return (pos[0]+1, pos[1]+1, direction)

instructions = parseInstructions(parsed[1])
minX, maxX, minY, maxY, grid = parseGrid(parsed[0])
endX, endY, endPos = traverse(instructions, (0,0))

if(endPos == 'RIGHT'):
    endPos = 0
elif(endPos == 'DOWN'):
    endPos = 1
elif(endPos == 'LEFT'):
    endPos = 2
else:
    endPos = '3'

print(1000*endY+4*endX+endPos)

# for row in range(minY, maxY+1):
#     for col in range(minX, maxX+1):
#         pos = (col, row)
#         if(pos not in grid):
#             print(' ', end='')
#         else:
#             print(grid[pos], end = '')
#     print()

