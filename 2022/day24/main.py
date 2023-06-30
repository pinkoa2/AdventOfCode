file = open('test.txt', 'r')
input = file.read().split('\n')
file.close()
input.pop(-1)

ROWS = len(input[0])
COLS = len(input)
'''
pos = ( x, y )
'''
startingPos = ( 1, 0 )
endingPos = ( COLS-1, ROWS-2 )
print(ROWS, COLS)
print(startingPos, endingPos)
blizzard = {}

def printGrid(grid):
    print('#'*COLS)
    for row in range(1, ROWS-1):
        print('#', end='')
        for col in range(1, COLS-1):
            pos = (col, row)
            if(pos not in grid):
                print('.', end='')
                continue
            if(len(grid[pos]) == 1):
                print(grid[pos][0], end='')
            else:
                print(len(grid[pos]), end='')
        print('#')
    print('#'*COLS)
    print()

def advanceBlizzard(grid):
    newGrid = {}
    for row in range(1, ROWS-1):
        for col in range(1, COLS-1):
            if((col, row) not in grid):
                continue
            for direction in grid[(col, row)]:
                if direction == '<':
                    newPos = (col - 1, row)
                    if(newPos[0] == 0):
                        newPos = ( COLS-2, row )
                    if(newPos not in newGrid):
                        newGrid[newPos] = ['<']
                    else:
                        newGrid[newPos].append('<')
                elif direction == '>':
                    newPos = (col + 1, row)
                    if(newPos[0] == COLS-1):
                        newPos = ( 1, row )
                    if(newPos not in newGrid):
                        newGrid[newPos] = ['>']
                    else:
                        newGrid[newPos].append('>')
                elif direction == '^':
                    newPos = (col, row-1)
                    if(newPos[1] == 0):
                        newPos = ( col, ROWS-2 )
                    if(newPos not in newGrid):
                        newGrid[newPos] = ['^']
                    else:
                        newGrid[newPos].append('^')
                else: # direction == 'v'
                    newPos = (col, row+1)
                    if(newPos[1] == ROWS-1):
                        newPos = ( col, 1 )
                    if(newPos not in newGrid):
                        newGrid[newPos] = ['v']
                    else:
                        newGrid[newPos].append('v')
    return newGrid

grid = {}
for row in range(ROWS):
    for col in range(COLS):
        if(input[row][col] == '.'):
            continue
        grid[ (col, row) ] = [input[row][col]]
printGrid(grid)

def checkSurrounds(pos, grid):
    positions = set()
    positions.add(pos)
    newPos = ( pos[0] - 1, pos[1])
    if (newPos[0] > 0 and newPos not in grid):
        positions.add(newPos)
    newPos = ( pos[0] + 1, pos[1])
    if (newPos[0] < COLS-1 and newPos not in grid):
        positions.add(newPos)
    newPos = ( pos[0], pos[1]-1)
    if (newPos[1] > 0 and newPos not in grid):
        positions.add(newPos)
    newPos = ( pos[0], pos[1]+1)
    if (newPos[1] < ROWS-1 and newPos not in grid):
        positions.add(newPos)
    return positions

pos = (1, 0)
current = set([pos])
time = 0
for i in range(5):
    grid = advanceBlizzard(grid)
    printGrid(grid)
# while(True):
#     next = set()
#     grid = advanceBlizzard(grid)
#     for pos in current
#         surrounding = getSurrounding(pos, grid)       
#         next = next.union(surrounding)
#     if( endingPos in next ):
#         break
#     next = current
#     time += 1

# print(time)
