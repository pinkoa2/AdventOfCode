
grid = []
with open('input.txt', 'r') as file:
    for line in file:
        grid.append(list(line.strip()))

def findRight(pos):
    startRow = pos[0]
    startCol = pos[1]
    treeHeight = int(grid[startRow][startCol])
    counter = 0
    for col in range(startCol+1, len(grid[0])):
        currentTree = int(grid[startRow][col])
        if(currentTree >= treeHeight):
            counter += 1
            break
        counter += 1
    return counter

def findLeft(pos):
    startRow = pos[0]
    startCol = pos[1]
    treeHeight = int(grid[startRow][startCol])
    counter = 0
    for col in range(startCol-1, -1, -1):
        currentTree = int(grid[startRow][col])
        if(currentTree >= treeHeight):
            counter += 1
            break
        counter += 1
    return counter

def findUp(pos):
    startRow = pos[0]
    startCol = pos[1]
    treeHeight = int(grid[startRow][startCol])
    counter = 0
    for row in range(startRow-1, -1, -1):
        currentTree = int(grid[row][startCol])
        if(currentTree >= treeHeight):
            counter += 1
            break
        counter += 1
    return counter

def findDown(pos):
    startRow = pos[0]
    startCol = pos[1]
    treeHeight = int(grid[startRow][startCol])
    counter = 0
    for row in range(startRow+1, len(grid), 1):
        currentTree = int(grid[row][startCol])
        if(currentTree >= treeHeight):
            counter += 1
            break
        counter += 1
    return counter

answer = 0
for row in range(len(grid)):
    for col in range(len(grid[row])):
        pos = (row, col)
        right = findRight(pos)
        left = findLeft(pos)
        up = findUp(pos)
        down = findDown(pos)
        result = right * left * down * up
        answer = max(answer, result) 

print(answer)
