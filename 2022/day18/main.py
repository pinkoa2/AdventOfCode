file = open('input.txt', 'r')
points = file.read().split('\n')
points.pop(-1)
file.close()

sides = {}
setPoints = set()

def mapPointsToSides(point):
    x = int(point[0])
    y = int(point[1])
    z = int(point[2])
    
    # Z faces positive side
    faces = []
    faces.append( (x+0.5, y+0.5, z+0.5) )
    faces.append( (x-0.5, y+0.5, z+0.5) )
    faces.append( (x+0.5, y-0.5, z+0.5) )
    faces.append( (x-0.5, y-0.5, z+0.5) )
    faces.sort()
    if( str(faces) not in sides):
        sides[(str(faces))] = 0
    sides[str(faces)] += 1
    
    # Z faces negative side
    faces = []
    faces.append( (x+0.5, y+0.5, z-0.5) )
    faces.append( (x-0.5, y+0.5, z-0.5) )
    faces.append( (x+0.5, y-0.5, z-0.5) )
    faces.append( (x-0.5, y-0.5, z-0.5) )
    faces.sort()
    if( str(faces) not in sides):
        sides[(str(faces))] = 0
    sides[str(faces)] += 1

    # X faces positive side
    faces = []
    faces.append( (x+0.5, y+0.5, z+0.5) )
    faces.append( (x+0.5, y-0.5, z+0.5) )
    faces.append( (x+0.5, y+0.5, z-0.5) )
    faces.append( (x+0.5, y-0.5, z-0.5) )
    faces.sort()
    if( str(faces) not in sides):
        sides[(str(faces))] = 0
    sides[str(faces)] += 1

    # X faces negative side
    faces = []
    faces.append( (x-0.5, y+0.5, z+0.5) )
    faces.append( (x-0.5, y-0.5, z+0.5) )
    faces.append( (x-0.5, y+0.5, z-0.5) )
    faces.append( (x-0.5, y-0.5, z-0.5) )
    faces.sort()
    if( str(faces) not in sides):
        sides[(str(faces))] = 0
    sides[str(faces)] += 1

    # Y faces positive side
    faces = []
    faces.append( (x+0.5, y+0.5, z+0.5) )
    faces.append( (x-0.5, y+0.5, z+0.5) )
    faces.append( (x+0.5, y+0.5, z-0.5) )
    faces.append( (x-0.5, y+0.5, z-0.5) )
    faces.sort()
    if( str(faces) not in sides):
        sides[(str(faces))] = 0
    sides[str(faces)] += 1
    
    # Y faces negative side
    faces = []
    faces.append( (x+0.5, y-0.5, z+0.5) )
    faces.append( (x-0.5, y-0.5, z+0.5) )
    faces.append( (x+0.5, y-0.5, z-0.5) )
    faces.append( (x-0.5, y-0.5, z-0.5) )
    faces.sort()
    if( str(faces) not in sides):
        sides[(str(faces))] = 0
    sides[str(faces)] += 1


maxX = 0
maxY = 0
maxZ = 0
minX = 10
minY = 10
minZ = 10
for point in points:
    p = point.split(',')
    x = int(p[0])
    y = int(p[1])
    z = int(p[2])
    setPoints.add((x, y, z))
    maxX = max(maxX, x)
    maxY = max(maxY, y)
    maxZ = max(maxZ, z)
    minX = min(minX, x)
    minY = min(minY, y)
    minZ = min(minZ, z)
    # mapPointsToSides(p)

print('X', minX, maxX)
print('Y', minY, maxY)
print('Z', minZ, maxZ)

def getSurround(point):
    x = int(point[0])
    y = int(point[1])
    z = int(point[2]) 
    points = set([
        (x+1, y, z),
        (x-1, y, z),
        (x, y+1, z),
        (x, y-1, z),
        (x, y, z+1),
        (x, y, z-1)
    ])
    return points

def outOfBounds(point):
    x = int(point[0])
    y = int(point[1])
    z = int(point[2]) 
    if( x < minX or x > maxX):
        return True
    if( y < minY or y > maxY):
        return True 
    if( z < minZ or z > maxZ):
        return True 
    return False

def grow(point):
    allPoints = set()
    allPoints.add(point)
    size = 0
    touchAir = False
    while(size != len(allPoints)):
        size = len(allPoints)
        surroundingPoints = set()
        for points in allPoints:
            surroundingPoints = surroundingPoints.union(getSurround(points))
        removePoints = set()
        for points in surroundingPoints:
            if(outOfBounds(points)):
                touchAir = True
                removePoints.add(points)
        surroundingPoints = surroundingPoints.difference(removePoints)
        surroundingPoints = surroundingPoints.difference(setPoints)
        allPoints = allPoints.union(surroundingPoints)
    return (touchAir, allPoints)

pointsThatTouchAir = set()
pointsThatDoNotTouchAir = set()
for x in range(minX, maxX+1):
    for y in range(minY, maxY+1):
        for z in range(minZ, maxZ+1):
            if( ((x,y,z) in setPoints) or ((x,y,z) in pointsThatTouchAir) or ((x,y,z) in pointsThatDoNotTouchAir)):
                continue
            touchAir, bubbleOfPoints = grow((x,y,z))
            if(touchAir):
                pointsThatTouchAir = pointsThatTouchAir.union(bubbleOfPoints)
            else:
                pointsThatDoNotTouchAir = pointsThatDoNotTouchAir.union(bubbleOfPoints)
# print(len(pointsThatDoNotTouchAir))
# print(len(pointsThatTouchAir))

setPoints = setPoints.union(pointsThatDoNotTouchAir)
for point in setPoints:
    mapPointsToSides(point)
result = 0
for side in sides:
    if(sides[side] == 1):
        result += 1
print(result)
