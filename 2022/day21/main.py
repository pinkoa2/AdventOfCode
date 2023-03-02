file = open('input.txt', 'r')
lines = file.read().split('\n')
lines.pop(-1)
file.close()

nameNumberMap = {}
toDo = {}

def doOperation(operation):
    num1 = operation[0]
    num2 = operation[2]
    if(num1 not in nameNumberMap or num2 not in nameNumberMap):
        return None

    cond = operation[1]
    if cond == '+':
        return nameNumberMap[num1] + nameNumberMap[num2]
    if cond == '-':
        return nameNumberMap[num1] - nameNumberMap[num2]
    if cond == '*':
        return nameNumberMap[num1] * nameNumberMap[num2]
    if cond == '/':
        return nameNumberMap[num1] / nameNumberMap[num2]


for line in lines:
    name = line.split(':')[0]
    operation = line.split(' ')
    if(len(operation) == 4):
        toDo[name] = ( operation[1], operation[2], operation[3] )   
    else:
        nameNumberMap[name] = int(operation[1])

while(len(toDo) > 0):
    remove = []
    for key in toDo:
        operation = toDo[key]
        value = doOperation(operation)
        if(value != None):
            nameNumberMap[key] = value
            remove.append(key)
    for i in remove:
        del toDo[i]



print(int(nameNumberMap['root']))
