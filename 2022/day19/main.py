file = open('input.txt', 'r')
blueprints = file.read().split('\n')
blueprints.pop(-1)
file.close()

class Blueprint():

    def __init__(self, state):
        self.ores = state[0]
        self.clay = state[1]
        self.obsidian = state[2]
        self.geodes = state[3]
        self.robotOre = state[4]
        self.robotClay = state[5]
        self.robotObsidian = state[6]
        self.robotGeode = state[7]
        self.robotOreCost = state[8]
        self.robotClayCost = state[9]
        self.obsidianOreCost = state[10]
        self.obsidianClayCost = state[11]
        self.geodeOreCost = state[12]
        self.geodeObsidianCost = state[13]
        
    def __str__(self):
        string = ''
        string += str(self.name) + '\n'
        string += str(self.robotOreCost) + '\n'
        string += str(self.robotClayCost) + '\n'
        string += str(self.obsidianOreCost) + ' ' + str(self.obsidianClayCost) + '\n'
        string += str(self.geodeOreCost) + ' ' + str(self.geodeObsidianCost)
        return string
    
    def collect(self):
        self.ores += self.robotOre
        self.clay += self.robotClay
        self.obsidian += self.robotObsidian
        self.geodes += self.robotGeode
    
    def getState(self):
        return (
            self.ores,
            self.clay,
            self.obsidian,
            self.geodes,
            self.robotOre,
            self.robotClay,
            self.robotObsidian,
            self.robotGeode,
            self.robotOreCost,
            self.robotClayCost,
            self.obsidianOreCost,
            self.obsidianClayCost,
            self.geodeOreCost,
            self.geodeObsidianCost
        )

    def copy(self):
        return Blueprint(self.getState())
    
    def buyRobotOre(self):
        bought = False
        if(self.ores >= self.robotOreCost):
            self.ores -= self.robotOreCost
            bought = True
        self.collect()
        if(bought):
            self.robotOre += 1

    def buyRobotClay(self):
        bought = False
        if(self.ores >= self.robotClayCost):
            self.ores -= self.robotClayCost
            bought = True
        self.collect()
        if(bought):
            self.robotClay += 1

    def buyRobotObsidian(self):
        bought = False
        if(self.clay >= self.obsidianClayCost and self.ores >= self.obsidianOreCost):
            self.ores -= self.obsidianOreCost
            self.clay -= self.obsidianClayCost
            bought = True
        self.collect()
        if(bought):
            self.robotObsidian += 1

    def buyRobotGeode(self):
        bought = False
        if(self.ores >= self.geodeOreCost and self.obsidian >= self.geodeObsidianCost):
            self.ores -= self.geodeOreCost
            self.obsidian -= self.geodeObsidianCost
            bought = True
        self.collect()
        if(bought):
            self.robotGeode += 1

def parse(blueprint):
        word1 = 'Each ore robot costs '
        word2 = ' ore. Each clay'
        robotOreCost = int(blueprint[ blueprint.index(word1)+len(word1) : blueprint.index(word2)+1])

        word1 = 'Each clay robot costs '
        word2 = ' ore. Each obsi'
        robotClayCost = int(blueprint[ blueprint.index(word1)+len(word1) : blueprint.index(word2)+1])

        word1 = 'Each obsidian robot costs '
        word2 = ' ore and '
        obsidianOreCost = int(blueprint[ blueprint.index(word1)+len(word1) : blueprint.index(word2)+1])

        word1 = 'ore and '
        word2 = ' clay.'
        obsidianClayCost = int(blueprint[ blueprint.index(word1)+len(word1) : blueprint.index(word2)+1])

        word1 = 'Each geode robot costs '
        index = blueprint.index(word1) + len(word1)
        index1 = blueprint.index(' ore and ', index)
        geodeOreCost = int(blueprint[ index : index1+1])

        index = blueprint.index(' ore and ', index) + len( ' ore and ')
        index1 = blueprint.index(' obsidian.') 
        geodeObsidianCost = int(blueprint[ index : index1+1])
        return Blueprint( (0,0,0,0,1,0,0,0,robotOreCost,robotClayCost,obsidianOreCost,obsidianClayCost,geodeOreCost,geodeObsidianCost) )

def recursive(depth, bp):
    numOfGeodes = bp.geodes
    if(depth > firstGeodeDepth[numOfGeodes+1]):
        return -1
    firstGeodeDepth[numOfGeodes] = min(firstGeodeDepth[numOfGeodes], depth)
    # if(len(states)%100000 == 0):
    #     print(len(states))
    newDepth = depth+1
    if(bp.getState() in states):
        return -1
    states.add(bp.getState())
    if(depth == 32):
        return bp.geodes

    newBp = bp.copy()
    newBp.buyRobotOre()
    r1 = recursive(newDepth, newBp)

    newBp = bp.copy()
    newBp.buyRobotClay()
    r2 = recursive(newDepth, newBp)

    newBp = bp.copy()
    newBp.buyRobotObsidian()
    r3 = recursive(newDepth, newBp)

    newBp = bp.copy()
    newBp.buyRobotGeode()
    r4 = recursive(newDepth, newBp)

    return max(r1, r2, r3, r4)

result = 1
for blueprint in blueprints:
    bp = parse(blueprint)
    states = set()
    firstGeodeDepth = dict()
    for i in range(32):
        firstGeodeDepth[i] = 1000000
    answer = recursive(0, bp)
    print(answer)
    result = result*answer
print(result)
