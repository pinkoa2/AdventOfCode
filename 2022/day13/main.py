import json
from functools import cmp_to_key

file = open('input.txt', 'r')
inputs = file.read().split('\n\n')
file.close()

def leftSideSmaller(left, right):
    if(isinstance(left, int) and isinstance(right, int)):
        if(left == right):
            return None
        return left < right

    newLeft = left
    if(isinstance(left, int)):
        newLeft = [left]
    newRight = right
    if(isinstance(right, int)):
        newRight = [right]
    
    for index in range(max(len(newLeft), len(newRight))):
        if(index >= len(newLeft)):
            return True
        if(index >= len(newRight)):
            return False

        check = leftSideSmaller(newLeft[index], newRight[index])
        if(check == None):
            continue
        return check

def compare(left, right):
    if(leftSideSmaller(left, right)):
        return -1
    return 1

allArrays = []
result = 0
for pair in range(len(inputs)):
    leftSide = json.loads(inputs[pair].split('\n')[0])
    rightSide = json.loads(inputs[pair].split('\n')[1])
    if(leftSideSmaller(leftSide, rightSide)):
        result += pair + 1
    allArrays.append(leftSide)
    allArrays.append(rightSide)
allArrays.append([[6]])
allArrays.append([[2]])

print(result)
allArrays.sort(key=cmp_to_key(compare))
allArrays.insert(0, 'NOTHING')
print( allArrays.index([[2]]) * allArrays.index([[6]]) )
