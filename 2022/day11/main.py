file = open('input.txt', 'r')
monkeys = file.read().split('\n\n')
file.close()


class Monkey:

    def __init__(self, parse):
        lines = parse.split('\n')
        self.items = []
        index = lines[1].index(':')
        self.items = lines[1][index+1:].split(',')
        self.items = [int(item) for item in self.items]
        index = lines[2].index('=')
        self.operation = lines[2][index+2:].split(' ')
        index = lines[3].index('by')
        self.divisible = int(lines[3][index+2:])
        self.TrueMonkey = int(lines[4][-1])
        self.FalseMonkey = int(lines[5][-1])
        self.iterations = 0

    def performSequenceOfOperations(self):
        for item in self.items:
            newItem = self.operationThing(item)
            newItem = newItem % 9699690 # all mods multiplies together (no idea how this mathly)
            if(newItem % self.divisible == 0):
                monkeyMap[self.TrueMonkey].items.append(newItem)
            else:
                monkeyMap[self.FalseMonkey].items.append(newItem)
            self.iterations += 1
        self.items = []
            

    def operationThing(self, value):
        num1 = self.convertNum(value, self.operation[0])
        num2 = self.convertNum(value, self.operation[2])
        if(self.operation[1] == '*'):
            return num1 * num2
        return num1 + num2

    def convertNum(self, value, num):
        if(num == 'old'):
            return int(value)
        return int(num)


    def printInfo(self):
        print(self.items)
        print(self.operation)
        print(self.divisible)
        print(self.TrueMonkey)
        print(self.FalseMonkey)

monkeyMap = {}
monkeyNumber = 0
for monkey in monkeys:
    monkeyMap[monkeyNumber] = Monkey(monkey)
    monkeyNumber += 1

for i in range(0,10000):
    for monkeyKey in monkeyMap:
        monkeyMap[monkeyKey].performSequenceOfOperations()


answer = []
for monkeyKey in monkeyMap:
    answer.append(monkeyMap[monkeyKey].iterations)

answer.sort()
print(answer[-1] * answer[-2])



