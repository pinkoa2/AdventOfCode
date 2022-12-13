import string

def letterToNumber(letter):
    letters = 'S' + string.ascii_lowercase + 'E'
    return letters.index(letter)


def searchShortestPath(pos, visited):
    pass
        
def getSurrounding(pos):
    up = (pos[0] + 1, pos[1])
    down = (pos[0] -1, pos[1])
    right = (pos[0], pos[1]+1)
    left = (pos[0], pos[1]-1)
    return [ up, down, right, left]

grid = {}
shortest = {}
with open('input.txt', 'r') as file:
    row = -1
    for line in file:
        row += 1
        col = -1
        for letter in line.strip():
            col += 1
            if(letter == 'S'):
                startPos = (row, col)
            if(letter == 'E'):
                endPos = (row, col)
            grid[ (row, col) ] = letterToNumber(letter)
            shortest[ (row, col) ] = 1000000


shortest[endPos] = 0
nextPos = [endPos]
while(len(nextPos) > 0):
    currentPos = nextPos.pop(0)
    surroundPos = getSurrounding(currentPos)
    for pos in surroundPos:
        if(pos not in grid):
            continue
        if(grid[currentPos] - grid[pos] <= 1 and shortest[currentPos] + 1 < shortest[pos]):
            shortest[pos] = shortest[currentPos] + 1
            nextPos.append(pos)

        



print(startPos)
print(endPos)
print(shortest[startPos])

minimum = 1000000
for pos in grid:
    if(grid[pos] == 1):
        minimum = min(minimum, shortest[pos])

print(minimum)
