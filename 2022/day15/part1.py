file = open('input.txt', 'r')
lines = file.read().split('\n')
lines.pop(-1)
file.close()


minX = 0
maxX = 0 
maxDist = 0

def getResult(y):
    result = 0
    buffer = maxDist+100

    for x in range(minX-buffer, maxX+buffer):
        for sensor in sensors:
            if(sensor.amIonSaveSpot((x, y))):
                result +=1 
                break
    return result
                
def distanceBetweenTwo(pos1, pos2):
    return abs(pos1[0]-pos2[0]) + abs(pos1[1] - pos2[1])

class Beacon():

    def __init__(self, pos):
        self.pos = pos

class Sensor():
    
    def __init__(self, pos, closestBeacon):
        global maxDist
        self.pos = pos
        self.closestBeacon = closestBeacon
        self.distFromSensorToBeacon = distanceBetweenTwo(pos, closestBeacon.pos)
        maxDist = max(maxDist, self.distFromSensorToBeacon)
    
    def amIonSaveSpot(self, pos):
        distToSensor = distanceBetweenTwo(pos, self.pos) 
        if(pos == self.closestBeacon.pos):
            return False
        if( distToSensor <= self.distFromSensorToBeacon ):
            return True
        return False


sensors = set()
beacons = set()
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
    minX = min(minX, sensorX, beaconX)
    maxX = max(maxX, sensorX, beaconX)

print(minX)
print(maxX)
print(maxDist)
result = getResult(2000000)
print(result)
