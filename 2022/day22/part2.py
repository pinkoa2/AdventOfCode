import json
fileName = 'test'
mapOfValues = open(f'./{fileName}/map.json')
mapAsString = mapOfValues.read().strip()
map = json.loads(mapAsString)

class Cube():

    def __init__(self):
        self.faces = {} 
