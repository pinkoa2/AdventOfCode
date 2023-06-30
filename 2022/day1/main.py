def addElfToTopThree(topThree, newElf):
    position = 0
    for elf in topThree:
        if newElf.getCalories() > elf.getCalories():
            break
        position += 1
    topThree.insert(position, newElf)
    if len(topThree) > 3:
        topThree.pop(-1)


class Elf:
    def __init__(self, name):
        self.calories = 0
        self.name = name

    def addCalories(self, calories):
        self.calories += calories

    def getCalories(self):
        return self.calories


f = open("input.txt", "r")


elfNum = 1
elf = Elf(elfNum)

topThree = []
for line in f:
    if line == "\n":
        addElfToTopThree(topThree, elf)
        elfNum += 1
        elf = Elf(elfNum)
        next
    num = line.strip()
    if num.isnumeric():
        elf.addCalories(int(line.strip()))

print(topThree[0].getCalories())
print(topThree[1].getCalories())
print(topThree[2].getCalories())
print(sum(elf.getCalories() for elf in topThree))
f.close()
