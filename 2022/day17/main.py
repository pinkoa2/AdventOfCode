file = open('input.txt')
jets = list(file.read().strip())
originalJets = jets
file.close()

ROCKS = [ 
    [ (0,0), (1,0), (2,0), (3,0) ],
    [ (1,0), (0,1), (1,1), (2,1), (1,2) ],
    [ (2,2), (2,1), (0,0), (1,0), (2,0) ],
    [ (0,0), (0,1), (0,2), (0,3) ],
    [ (0,0), (0,1), (1,0), (1,1) ]
]

savedStates ={} 

RIGHT = 'RIGHT'
LEFT = 'LEFT'
DOWN = 'DOWN'

def getDirection():
    letter = jets.pop(0)
    jets.append(letter)
    if(letter == '>'):
        return RIGHT
    return LEFT

def getRock(y):
    positions = ROCKS.pop(0)
    ROCKS.append(positions)
    newPositions = []
    for pos in positions:
        newPositions.append( ( 2 + pos[0], pos[1] + y) )
    rock = Rock(newPositions) 
    return rock

class Rock():
    def __init__(self, positions):
        self.positions = positions
        
    def moveDown(self):
        newPositions = []
        for pos in self.positions:
            if((pos[0], pos[1]-1) in grid):
                return False
            newPositions.append( (pos[0], pos[1]-1) )
        self.positions = newPositions
        return True

    def moveRight(self):
        newPositions = []
        for pos in self.positions:
            if((pos[0]+1, pos[1]) in grid or pos[0]+1 >= 7):
                return False
            newPositions.append( (pos[0]+1, pos[1]) )
        self.positions = newPositions
        return True

    def moveLeft(self):
        newPositions = []
        for pos in self.positions:
            if((pos[0]-1, pos[1]) in grid or pos[0]-1 < 0):
                return False
            newPositions.append( (pos[0]-1, pos[1]) )
        self.positions = newPositions
        return True

    def move(self, MOVE):
        if(MOVE == RIGHT):
            return self.moveRight()
        if(MOVE == LEFT):
            return self.moveLeft()
        if(MOVE == DOWN):
            return self.moveDown()

    def getTopY(self):
        topY = 0
        for pos in self.positions:
            topY = max(topY, pos[1])
        return topY

    def addRockToGrid(self):
        for pos in self.positions:
            grid.add(pos)

            

grid = set()
for i in range(7):
   grid.add((i, 0)) 
topY = 0

numOfRocks = 0
five = 0
done = False
savedYs = []
while(numOfRocks < 5000):
    if(done):
        break
    numOfRocks += 1
    rock = getRock(topY + 4)
    while(True):
        direction = getDirection()
        rock.move(direction)
        safe = rock.move(DOWN)
        if(not safe):
            topY = max(topY, rock.getTopY())
            rock.addRockToGrid()
            break
    state = ''
    for i in range(7):
        if( (i, topY) in grid ):
            state += '.'
        else:
            state += '#'
    state += str(jets)
    if(state in savedStates):
        five += 1
        savedYs.append(topY)
        print(numOfRocks, topY, savedStates[state])
        # if(five == 5):
        #     done = True
        #     break
    else:
        savedStates[state] = numOfRocks
print(numOfRocks, topY)

for y in range(60, 49, -1):
    for x in range(7):
        if( (x, y) in grid):
            print('#', end='')
            continue
        print('.', end='')
    print()
print()
for y in range(10, -1, -1):
    for x in range(7):
        if( (x, y) in grid):
            print('#', end='')
        else:
            print('.', end='')
    print()
        
ROCKS = [ 
    [ (0,0), (1,0), (2,0), (3,0) ],
    [ (1,0), (0,1), (1,1), (2,1), (1,2) ],
    [ (2,2), (2,1), (0,0), (1,0), (2,0) ],
    [ (0,0), (0,1), (0,2), (0,3) ],
    [ (0,0), (0,1), (1,0), (1,1) ]
]

jets = originalJets
remaining = 1000000000000 % (numOfRocks) 
result = (1000000000000 // (numOfRocks)) * topY

grid = set()
for i in range(7):
   grid.add((i, 0)) 
topY = 0

numOfRocks = 0
while(numOfRocks < remaining):
    numOfRocks += 1
    rock = getRock(topY + 4)
    while(True):
        direction = getDirection()
        rock.move(direction)
        safe = rock.move(DOWN)
        if(not safe):
            topY = max(topY, rock.getTopY())
            rock.addRockToGrid()
            break
print(topY)
print(result + topY)
 '''
Bunch of paper work
3129+2634*589970500+754


 ''''
