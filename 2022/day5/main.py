
crates = [
    ['N', 'Z'],
    ['D', 'C', 'M'],
    ['P']
]

crates = [
    ['F', 'T', 'N', 'Z', 'M', 'G', 'H', 'J'],
    ['J', 'W', 'V'],
    ['H', 'T', 'B', 'J', 'L', 'V', 'G'],
    ['L', 'V', 'D', 'C', 'N', 'J', 'P', 'B'],
    ['G', 'R', 'P', 'M', 'S', 'W', 'F'],
    ['M', 'V', 'N', 'B', 'F', 'C', 'H', 'G'],
    ['R', 'M', 'G', 'H', 'D'],
    ['D', 'Z', 'V', 'M', 'N', 'H'],
    ['H', 'F', 'N', 'G']
]


class Stack():

    def __init__(self, stack):
        self.array = stack

    def addCrate(self, crate):
        self.array.insert(0, crate)

    def removeCrate(self):
        return self.array.pop(0)

    def removeCrates(self, amount):
        crates = []
        for _ in range(amount):
            crates.append(self.removeCrate())
        return crates

    def addCrates(self, crates):
        for crate in crates:
            self.addCrate(crate)



class Stacks():

    def __init__(self, crates):
        self.stackMap = {}
        nameOfIndex = 1
        for stack in crates:
            self.stackMap[nameOfIndex] = Stack(stack)
            nameOfIndex += 1

    def followInstructions(self, instructions):
        amount = instructions[0]
        start = instructions[1]
        end = instructions[2]
        crates = self.stackMap[start].removeCrates(amount)
        crates.reverse()
        self.stackMap[end].addCrates(crates)

    def getString(self):
        string = ''
        for key in self.stackMap:
            string += self.stackMap[key].removeCrate()
        return string

        
def readInstructionsFromLine(line):
    result = []
    firstIndex = 0
    for i in range(2):
        firstIndex = line.index(' ', firstIndex)
        secondIndex = line.index(' ', firstIndex+1)
        result.append(int(line[firstIndex+1:secondIndex]))
        firstIndex = secondIndex+1
    result.append(int(line[line.index(' ', firstIndex)+1:]))
    return result



stacks = Stacks(crates)

fileName = 'input.txt'
with open(fileName, 'r') as file:
    for line in file:
        cleanLine = line.strip()
        instructions = readInstructionsFromLine(cleanLine)
        stacks.followInstructions(instructions)
        
print(stacks.getString())
