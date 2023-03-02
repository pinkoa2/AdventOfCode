file = open('input.txt', 'r')
lines = file.read().split('\n')
lines.pop(-1)
file.close()

class Valve():
    def __init__(self, name, flow, tunnels):
        self.name = name
        self.flow = flow
        self.tunnels = tunnels

allValves = {}

for line in lines:
    name = line[ line.index(' ') + 1 : line.index('h') - 1 ]
    rate = int(line[ line.index('=') + 1 : line.index(';') ])
    valveIndex = line.index('valve')
    tunnels = line[ line.index(' ', valveIndex)+1 :].split(', ')
    allValves[name] = Valve(name, rate, tunnels)

states = {}
def findMaxFlow(valve, elephantValve, depth, opened):
    if(depth <= 0):
        return 0

    newDepth = depth - 1
    sorte = list(opened)
    sorte.sort()
    key = (valve.name, elephantValve.name, depth, str(sorte))
    if(key in states):
        return states[key]

    results = []
    # Choose to open
    if(valve.name not in opened and valve.flow != 0): # you cannot open so must skip this whole condition
        newOpened = opened.copy()
        newOpened.add(valve.name)
        
        # Elephant opens
        if(elephantValve.name not in newOpened and elephantValve.flow != 0):
            anotherOpen = newOpened.copy()
            anotherOpen.add(elephantValve.name)
            results.append( valve.flow*newDepth + 
                    elephantValve.flow*newDepth + findMaxFlow(valve, elephantValve, newDepth, anotherOpen))
        # Elephant does not open
        for newElephantValveName in elephantValve.tunnels:
            newElephantValve = allValves[newElephantValveName]
            results.append( valve.flow*newDepth + 
                    findMaxFlow(valve, newElephantValve, newDepth, newOpened))
        
    # Choose to move to next
    for newValveName in valve.tunnels:
        newOpened = opened.copy()
        newValve = allValves[newValveName]

        # Elephant opens
        if(elephantValve.name not in newOpened and elephantValve.flow != 0):
            anotherOpen = newOpened.copy()
            anotherOpen.add(elephantValve.name)
            results.append( elephantValve.flow*newDepth + 
                    findMaxFlow(newValve, elephantValve, newDepth, anotherOpen))
            
        # Elephant does not open
        for newElephantValveName in elephantValve.tunnels:
            newElephantValve = allValves[newElephantValveName]
            results.append(findMaxFlow(newValve, newElephantValve, newDepth, newOpened))

    ans = max(results)
    states[key] = ans

    return ans

result = findMaxFlow(allValves['AA'], allValves['AA'], 26, set())
print(result)

