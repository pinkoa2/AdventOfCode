
f = open('input.txt', 'r')
string = f.read().strip()

print(len(string))

for i in range(14, len(string)):
    value = set(list(string[i-14:i]))
    if(len(value) == 14):
        print(string[i-14:i])
        print(i)
        break
