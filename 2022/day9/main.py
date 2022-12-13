

class Node():

    def __init__(self):
        self.pos = (0,0)
        self.visited = [self.pos]

    def doWeTouch(self, other):
        if(abs(self.pos[0] - other.pos[0]) <= 1 and abs(self.pos[1] - other.pos[1]) <= 1):
            return True
        return False

    def move(self, move):
        pos = self.pos
        if(move == 'U'):
            self.pos = ( pos[0], pos[1] - 1)
        if(move == 'D'):
            self.pos = ( pos[0], pos[1] + 1)
        if(move == 'R'):
            self.pos = ( pos[0] + 1, pos[1])
        if(move == 'L'):
            self.pos = ( pos[0] - 1, pos[1])
        self.visited.append(self.pos)

    def followHead(self, head):
        headPos = head.pos
        if(self.doWeTouch(head)):
            return
        xDist = self.pos[0] - headPos[0]
        yDist = self.pos[1] - headPos[1]
        if(xDist != 0):
            if(xDist < 0):
                self.pos = (self.pos[0] + 1, self.pos[1])
            if(xDist > 0):
                self.pos = (self.pos[0] - 1, self.pos[1])
        if(yDist != 0):
            if(yDist < 0):
                self.pos = (self.pos[0], self.pos[1] + 1)
            if(yDist > 0):
                self.pos = (self.pos[0], self.pos[1] - 1)
        self.visited.append(self.pos)


file = open('input.txt', 'r')
instructions = file.read().split('\n')
file.close()

instructions.pop(-1)


nodes = []
for i in range(10):
    nodes.append(Node())

for instruction in instructions:
    clean = instruction.split(' ')
    print(clean)
    move = clean[0]
    times = int(clean[1])

    for _ in range(times):
        head = nodes[0]
        head.move(move)
        for i in range(1, 10):
            tail = nodes[i]
            tail.followHead(head)
            head = tail












print(len(set(nodes[9].visited)))
