f = open('input.txt', 'r')
instructions = f.read().split('\n')
f.close()
global result
result = 0


class Grid():
    def __init__(self):
        self.grid = []
        for i in range(6):
            temp = []
            for i in range(40):
                temp.append('.')
            self.grid.append(temp)
    
    def moveSrite(self, cycle, reg):
        self.sprite = []
        row = cycle // 40
        col = reg - 1
        self.sprite.append( (row, col) )
        self.sprite.append( (row, col+1) )
        self.sprite.append( (row, col+2) )



    def place(self, cycle):
        row = cycle // 40
        col = cycle % 40 - 1
        if((row, col) in self.sprite):
            self.grid[row][col] = '#'
        self.grid[0][0] = "#"

    def __str__(self):
        sting= ''
        for i in self.grid:
            for j in i:
                sting += j
            sting += '\n'

        return sting

grid = Grid()

class Tube():

    def __init__(self):
        self.cycle = 1
        self.value = 1
        self.tasks = dict()

    def completeCycle(self):
        if(self.cycle in self.tasks):
            self.value += self.tasks[self.cycle]
            self.hasTask = False
        self.cycle += 1
        print(self.cycle, self.value)
        grid.moveSrite(self.cycle, self.value)
        grid.place(self.cycle)


    def addTask(self, i, amount):
        self.tasks[self.cycle+i] = amount
        self.hasTask = True
    
    def cycleTask(self):
        while(self.hasTask):
            self.completeCycle()

tube = Tube()
for line in instructions:
    instruction = line.split(' ') 
    if(instruction[0] == 'addx'):
        tube.addTask(1, int(instruction[1]))
    if(instruction[0] == 'noop'):
        tube.addTask(0, 0)

    tube.cycleTask()
    # print(instruction)
    # print(tube.cycle, tube.value)

    # cycle = tube.cycle
    # if(cycle == 20 or (cycle-20) % 40 == 0):
    #     print(cycle, tube.value)
    #     result += cycle * tube.value



print(str(grid))
