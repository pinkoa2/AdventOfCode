file = open('test.txt', 'r')
lines = file.read().split('\n')
lines.pop(-1)
file.close()


class Valve():

    def __init__(self, name, flow, tunnels):
        self.name = name
        self.flow = flow
        self.tunnels = tunnels

allValves = {}
nonZeroValves = set()

for line in lines:
    name = line[ line.index(' ') + 1 : line.index('h') - 1 ]
    rate = int(line[ line.index('=') + 1 : line.index(';') ])
    valveIndex = line.index('valve')
    tunnels = line[ line.index(' ', valveIndex)+1 :].split(', ')
    allValves[name] = Valve(name, rate, tunnels)
    if(rate != 0):
        nonZeroValves.add(name)


MAX_DEPTH = 30 
def findMaxFlow(valve, depth, currentValue, cumulativeValue, opened):
    if(depth >= MAX_DEPTH+1):
        return cumulativeValue 
    if(len(nonZeroValves.difference(opened)) == 0):
        return cumulativeValue

    results = []
    # Choose to open
    if(valve.name not in opened and valve.flow != 0): # you cannot open so must skip this whole condition
        newOpened = opened.copy()
        newOpened.add(valve.name)
        newDepth = depth + 2
        newCurrentValue = currentValue + valve.flow
        newCumulativeValue = cumulativeValue + newCurrentValue
        results.append( findMaxFlow(valve, newDepth, newCurrentValue, newCumulativeValue, newOpened) )
        
    # Choose to move to next
    for newValveName in valve.tunnels:
        newValve = allValves[newValveName]
        newDepth = depth + 1
        newCumulativeValue = cumulativeValue + currentValue
        results.append(findMaxFlow(newValve, newDepth, currentValue, newCumulativeValue, opened))

    return max(results) 

result = findMaxFlow(allValves['AA'], 1, 0, 0, set())
print(result)

