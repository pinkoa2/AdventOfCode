import string

fileName = 'input.txt'

def findCommon(set1, set2, set3):
    intersection = set1.intersection(set2).intersection(set3)
    return intersection.pop()

def letterToNum(letter):
    letters = string.ascii_letters
    return letters.index(letter) + 1 

sacks = []
result = 0
with open(fileName, 'r') as file:
    for line in file:
        sack = line.strip()
        sacks.append(set(list(sack)))


for i in range(0, len(sacks) - 2, 3):
    sack1 = sacks[i]
    sack2 = sacks[i+1]
    sack3 = sacks[i+2]
    # print(sack1)
    # print(sack2)
    # print(sack3)
    # print(findCommon(sack1, sack2, sack3))
    result += letterToNum(findCommon(sack1, sack2, sack3))

print(result)
