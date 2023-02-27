fileName = 'test.txt'

class Blizzard:

    def __init__(self, fileName):
        file = open(fileName, 'r')
        self.grid = {}
        self.parse(file)
        file.close()

    def parse(self, file):
        rows = file.read().split('\n')
        rows.pop(-1)
        for y in range(len(rows)):
            for x in range(len(rows[y])):
                self.grid[ (x, y) ] = [rows[y][x]]
        self.minX = 0
        self.minY = 0
        self.maxX = x+1
        self.maxY = y+1

    def __str__(self):
        string = ''
        for y in range( self.minY, self.maxY ):
            for x in range( self.minX, self.maxX ):
                length = len(self.grid[(x,y)])
                if(length == 1):
                    value = self.grid[(x,y)][0]
                else:
                    value = str(length)
                string += value
            string += '\n'
        return string
    
blizzard = Blizzard(fileName)
