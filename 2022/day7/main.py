listOfAllDirectories = []



class Directories:

    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.directories = {}
        self.files = {}
        self.size = 0
        listOfAllDirectories.append(self)

    def updateParents(self, amount):
        self.size += amount
        if(self.parent == None):
            return
        self.parent.updateParents(amount)

    def executeChangeDirectory(self, cdCommand):
        if(cdCommand == '..'):
            return self.parent
        return self.directories[cdCommand]

    def executeList(self, command):
        if(command[0] == 'dir'):
            self.directories[command[1]] = Directories(self, command[1])
        else:
            # self.size += int(command[0])
            self.updateParents(int(command[0]))
            self.files[command[1]] = command

with open('input.txt', 'r') as file:
    allLines = file.read().split('\n')

current = Directories(None, '/')

allLines.pop(0)
allLines.pop(-1)

for line in allLines:
    
    command = line.split(' ')

    if(command[0] == '$'):

        if(command[1] == 'cd'):
            current = current.executeChangeDirectory(command[2])
            continue

        # if(command[1] == 'ls'):
        #     current.executeList()
    else:
        current.executeList(command)


result = 0
for directory in listOfAllDirectories:
    if(directory.size <= 100000):
        result += directory.size

print(result)

print(len(listOfAllDirectories))

totalMemory = 70000000 - listOfAllDirectories[0].size
neededMemory = 30000000 - totalMemory

def findMinumumToRemove(directory):
    global minimum
    if(directory.size < neededMemory):
        return
    if(directory.size >= neededMemory and directory.size < minimum):
        minimum = directory.size
    for key in directory.directories:
        findMinumumToRemove(directory.directories[key])
global minimum
minimum = 70000000
findMinumumToRemove(listOfAllDirectories[0])

print(minimum)
