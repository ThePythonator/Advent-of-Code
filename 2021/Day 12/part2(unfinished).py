def get_starting(lines, start):
    return [line for line in lines if line[0] == start] + [[line[1],line[0]] for line in lines if line[1] == start]

def get_starting_excluding(lines, start, excluding):
    return [line for line in get_starting(lines, start) if line[1] not in excluding]

def get_paths_excluding(lines, start, excluding, twice):
    paths = []
    connections = get_starting(lines, start) if twice else get_starting_excluding(lines, start, excluding)
    if not twice:
        print('-----------')
        print(start)
        print(excluding)
        input(connections)
    for connection in connections:
        if connection[1] == 'start':
            continue
        elif connection[1] == 'end':
            paths.append(','.join(connection))
        else:
            t = twice
            ex = excluding.copy()
            
            if start.islower():
                if t and start in ex:
                    t = False
                else:
                    ex += [start]
                
            for path in get_paths_excluding(lines, connection[1], ex, t):
                paths.append(start+','+path)
    return paths

with open('input2.txt') as f:
    lines = [line.strip().split('-') for line in f.readlines()]

##lines = [
##    ['start','A'],
##    ['start','b'],
##    ['A','c'],
##    ['A','b'],
##    ['b','d'],
##    ['A','end'],
##    ['b','end']
##]

paths = get_paths_excluding(lines, 'start', [], True)

print(len(paths))
for line in paths: print(line)
