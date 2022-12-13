
class Sections:

    def __init__(self, sectionRange):
        self.sectionRange = sectionRange
        sectionsSplits = sectionRange.split('-')
        self.min = int(sectionsSplits[0])
        self.max = int(sectionsSplits[1])
        self.makeIntersection()

    def makeIntersection(self):
        self.set = set()
        for i in range(self.min, self.max+1, 1):
            self.set.add(i)

    def isOverlap(self, otherSection):
        value = False
        overlap = self.set.intersection(otherSection.set)
        if(len(overlap) >= min(len(self.set), len(otherSection.set)) ):
            value = True
        absoluteMin = min(self.min, otherSection.min)
        absoluteMax = max(self.max, otherSection.max)
        if(absoluteMin == self.min and absoluteMax == self.max):
            if(value==False):
                print(self.min, self.max, otherSection.min, otherSection.max)
            value=True
        if(absoluteMin == otherSection.min and absoluteMax == otherSection.max):
            if(value==False):
                print(self.min, self.max, otherSection.min, otherSection.max)
            value=True
        return value


# fileName = 'input.txt'
# result = 0
# with open(fileName, 'r') as file:
#     for line in file:
#         clean = line.strip()
#         inputs = clean.split(',')
#         # if(inputs[0] == inputs[1]):
#         #     print('skipping...')
#         #     continue
#         s1 = Sections(inputs[0])
#         s2 = Sections(inputs[1])
#         if(s1.isOverlap(s2)):
#             result += 1
#         # print(clean, result)

# print(result)

