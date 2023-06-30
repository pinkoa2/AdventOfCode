file = open('input.txt', 'r')
lines = file.read().split('\n')
lines.pop(-1)
file.close()

nameNumberMap = {}
toDo = {}

opposite = {
    "+": '-',
    '-': '+',
    '*': '/',
    '/': '*'
}    

def doOperation(num1, num2, cond):
    if cond == '+':
        return num1 + num2
    if cond == '-':
        return num1 - num2
    if cond == '*':
        return num1 * num2
    if cond == '/':
        return num1 / num2

def doLeft(num1, num2, cond):
    if(cond == '+'):
        return num1 - num2
    if(cond == '-'):
        return -1 * (num1 - num2)
    if(cond == "*"):
        return num1 / num2
    if(cond == '/'):
        return (num2/num1)

class Nodes():

    def __init__(self, name):
        self.name = name
        if(name in nameNumberMap):
            self.value = nameNumberMap[name]
            self.right = None
            self.left = None
            self.operation = None
        else:
            operation = toDo[name]
            self.left = Nodes(operation[0])
            self.operation = operation[1]
            self.right = Nodes(operation[2])
            self.value = None
    
    def calculate(self):
        if(self.value == None and self.right == None):
            return
        if(self.left.value == None and self.left != None):
            self.left.calculate()
        if(self.right.value == None and self.right != None):
            self.right.calculate()

        if(self.right.value == None or self.left.value == None):
            return

        cond = self.operation
        if cond == '+':
            self.value = self.left.value + self.right.value
        if cond == '-':
            self.value = self.left.value - self.right.value
        if cond == '*':
            self.value = self.left.value * self.right.value
        if cond == '/':
            self.value = self.left.value / self.right.value


for line in lines:
    name = line.split(':')[0]
    operation = line.split(' ')
    if(len(operation) == 4):
        toDo[name] = ( operation[1], operation[2], operation[3] )   
    else:
        nameNumberMap[name] = int(operation[1])

nameNumberMap['humn'] = None
rootNode = Nodes('root')
rootNode.calculate()
result = 0
if(rootNode.right.value == None):
    result = rootNode.left.value
else:
    result = rootNode.right.value

node = rootNode
result = result * 2
while(True):
    if(node.right == None and node.left == None):
        print(node.name, result)
        break
    # Unknown is right
    if(node.right.value == None):
        result = doLeft(result, node.left.value, node.operation)
        node = node.right
        continue        
    # Unknown is left 
    if(node.left.value == None):
        result = doOperation(result, node.right.value, opposite[node.operation])         
        node = node.left 
        continue


