file = open('input.txt', 'r')
lines = file.read().split('\n')
lines.pop(-1)
file.close()

CONDITION = 4000000

allBorders = set()

def distanceBetweenTwo(pos1, pos2):
    return abs(pos1[0]-pos2[0]) + abs(pos1[1] - pos2[1])

def addConditions(border, pos):
    if( 0 <= pos[0] <= CONDITION and 0 <= pos[1] <= CONDITION):
        doIadd = True
        for sensor in sensors:
            if(sensor.amIWithinTheSensor(pos)):
                doIadd = False
        if(doIadd):
            border.add(pos)

def getBorders(pos, radius):
    borders = set()
    x = pos[0]
    y = pos[1]
    for i in range(radius):
        addConditions( borders, (x-radius-1+i, y-i) )
        addConditions( borders, (x-radius-1+i, y+i) )
        addConditions( borders, (x+radius+1-i, y-i) )
        addConditions( borders, (x+radius+1-i, y+i) )
    return borders

def pruneBorders(sensor):
    remove = set()
    for pos in allBorders:
        if(sensor.amIWithinTheSensor(pos)):
            remove.add(pos)
    for pos in remove:
        allBorders.remove(pos)
    
def combineBorders(border, sensor):
    global allBorders
    pruneBorders(sensor)
    allBorders = allBorders.union(border)


class Beacon():

    def __init__(self, pos):
        self.pos = pos

class Sensor():
    
    def __init__(self, pos, closestBeacon):
        self.pos = pos
        self.closestBeacon = closestBeacon
        self.distFromSensorToBeacon = distanceBetweenTwo(pos, closestBeacon.pos)
        self.addBorders()

    def addBorders(self):
        borders = getBorders(self.pos, self.distFromSensorToBeacon)
        combineBorders(borders, self) 

    def amIWithinTheSensor(self, pos):
        distToSensor = distanceBetweenTwo(pos, self.pos) 
        if( distToSensor <= self.distFromSensorToBeacon ):
            return True
        return False
    
sensors = set()
beacons = set()
counter = 0
for line in lines:
    sensorX = int(line[ line.index('x=')+2 : line.index(',') ])
    sensorY = int(line[ line.index('y=')+2 : line.index(':') ])
    sep = line.index(':')
    beaconX = int( line[ line.index('x=', sep)+2 : line.index(',', sep) ])
    beaconY = int( line[ line.index('y=', sep)+2 :])
    beacon = Beacon( (beaconX, beaconY) )
    beacons.add(beacon)
    sensor = Sensor( (sensorX, sensorY), beacon )
    sensors.add(sensor)
    print("sensor", counter)
    counter += 1

print(len(allBorders))
pos = allBorders.pop()
print( pos[0] * 4000000 + pos[1])
