with open('in.txt') as f:
    lines = [line.strip() for line in f.readlines()]

rules = {}

for line in lines:
    colour = ' '.join(line.split(' ')[:2])

    contentsString = ' '.join(line.split(' ')[4:])[:-1]

    rules[colour] = {}

    for c in contentsString.split(', '):
        if c.split(' ')[0] != 'no':
            count = int(c.split(' ')[0])
            cColour = ' '.join(c.split(' ')[1:3])
            rules[colour][cColour] = count

def recurse(target, rules):
    parents = []
    for colour in rules:
        if target in rules[colour]:
            parents.append(colour)
    return parents


##def recursive(start, rules):
##    colours = []
##    results = recurse(start, rules)
##    for colour in results:
##        if colour not in colours:
##            colours.append(colour)
##            
##        results = recurse(colour, rules)
##        if results != []:
####            print(results)
##            c = recursive(colour, rules)
##
##    return colours

def recursive(start, rules):
    colours = []
    results = recurse(start, rules)
    if results == []:
        return colours
    
    for colour in results:
        colours.append(colour)
            
        colours += recursive(colour, rules)

    return colours

##colours = recursive('shiny gold', rules)
##print(colours,len(set(colours)))

def r(start, rules):
    total = 0
    results = rules[start]
    if results == {}:
        return total
    for colour in results:
        total += rules[start][colour]
        total += rules[start][colour]*r(colour, rules)
    return total

print(r('shiny gold', rules))
