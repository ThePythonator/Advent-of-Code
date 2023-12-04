with open('in.txt') as f:
    lines = f.readlines()

resLines = []
for line in lines:
    resLines.append(line.strip())

totalValid = 0
for line in resLines:
    rule,password = line.split(': ')
    rangeCount,rangeChar = rule.split(' ')
    minCount,maxCount = rangeCount.split('-')
    minCount,maxCount = int(minCount),int(maxCount)

##    rangeCharOccurance = 0
##    for c in password:
##        if c == rangeChar:
##            rangeCharOccurance += 1

##    if rangeCharOccurance >= minCount and rangeCharOccurance <= maxCount:
##        totalValid += 1

    num = 0
    num += 1 if password[minCount-1] == rangeChar else 0
    num += 1 if password[maxCount-1] == rangeChar else 0
    if num == 1:
        totalValid += 1

print(totalValid)
