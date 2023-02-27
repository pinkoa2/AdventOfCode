import math

def getStartingPos(decimal):
    starting = '1=' 
    while(True):
        num = convertSnafuToDecimal(starting)
        if(num > decimal):
            return starting[:-1]
        starting += '='

def logBase5(decimal):
    return int(math.log(decimal, 5))

def convertDecimalToSnafu(decimal):
    current = getStartingPos(decimal)

    while(convertSnafuToDecimal(current) != decimal):
        value = convertSnafuToDecimal(current) 
        difference = decimal - value
        exp = logBase5(difference)
        current = increaseByExp(current, exp)
    
    return current

def getNextValue(value):
    if(value == '2'):
        return '='
    values = '=-012'
    index = values.index(value)
    return values[index+1]


def increaseByExp(original, exp):
    snafu = list(revertString(original))

    for i in range(exp, len(snafu)):
        snafu[i] = getNextValue(snafu[i])
        if(snafu[i] == '='):
            continue
        return revertString(''.join(snafu))

    return '1'+'='*len(original)

def revertString(string):
    return string[::-1]

def convertSymbolToValue(symbol):
    if(symbol == '='):
        return -2
    if(symbol == '-'):
        return -1
    return int(symbol)

def convertSnafuToDecimal(string):
    snafu = revertString(string)
    result = 0
    for index in range(len(snafu)):
        result += 5**index * convertSymbolToValue(snafu[index]) 
    return result

file = open('input.txt', 'r')
lines = file.read().split('\n')
lines.pop(-1)

answer = 0
for line in lines:
    value = line.strip()
    answer += convertSnafuToDecimal(value)

print(answer)

result = convertDecimalToSnafu(answer)
print(result)

