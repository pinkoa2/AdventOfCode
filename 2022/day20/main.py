import uuid

file = open('input.txt', 'r')
numbers = file.read().split('\n')
numbers.pop(-1)
file.close()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])*811589153

keys = {}
order = []
for num in numbers:
    uniqueKey =str(uuid.uuid4())
    keys[uniqueKey] = int(num)
    order.append(uniqueKey)

array = order.copy()

for _ in range(10):
    for key in order:
        removeIndex = array.index(key)
        array.pop(removeIndex)
        index = (keys[key]+removeIndex) % len(array)
        
        if(keys[key] < 0 and index == 0):
            array.append(key)
        else:
            array.insert(index, key)
result = 0
for key in keys:
    if(keys[key] == 0):
        zeroKey = key
zeroIndex = array.index(zeroKey)
print(zeroIndex)
for i in range(1,4):
    index = (i*1000+zeroIndex) % len(array)
    print(index, keys[array[index]])
    result += keys[array[index]]

print(result)

