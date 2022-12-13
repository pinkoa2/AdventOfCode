grid = []
trees = set()
with open('input.txt', 'r') as file:
    for line in file:
        grid.append(list(line.strip()))

def grabRowRight(row):
    return grid[row]

def grabColumnDown(col):
    r = []
    for row in range(len(grid)):
        r.append(grid[row][col])
    return r

def traverseRow(row, rowIndex):
    seen = set([-1])
    for i in range(len(row)-1, -1, -1):
        treeHeight = int(row[i])
        if(treeHeight > max(seen)):
            trees.add((rowIndex, i))
        # if(treeHeight == 1):
        #     print(seen)
        seen.add(treeHeight)

    seen = set([-1])
    for i in range(len(row)):
        treeHeight = int(row[i])
        if(treeHeight > max(seen)):
            trees.add((rowIndex, i))
        seen.add(treeHeight)

def traverseCol(col, colIndex):
    seen = set([-1])
    for i in range(len(col)-1, -1, -1):
        treeHeight = int(col[i])
        if(treeHeight > max(seen)):
            trees.add((i, colIndex))
        seen.add(treeHeight)

    seen = set([-1])
    for i in range(len(col)):
        treeHeight = int(col[i])
        if(treeHeight > max(seen)):
            trees.add((i, colIndex))
        seen.add(treeHeight)

# Look at Rows
for i in range(len(grid)):
    row = grabRowRight(i)
    traverseRow(row, i)

# Look at Cols
for i in range(len(grid[0])):
    col = grabColumnDown(i)
    traverseCol(col, i)

for tree in trees:
    # if(tree[0] == 0 or tree[0] == 4):
    #     continue
    # if(tree[1] == 0 or tree[1] == 4):
    #     continue
    print(tree)
print(len(trees))
