import itertools

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

distances = {}

for line in lines:
    l = line.split(' ')
    s = l[0]
    e = l[2]
    d = int(l[4])

    if s not in distances.keys():
        distances[s] = {}
    
    if e not in distances.keys():
        distances[e] = {}

    distances[s][e] = d
    distances[e][s] = d

result = 0

p = itertools.permutations(distances.keys())

for t in p:
    r = 0
    for i in range(len(t) - 1):
        r += distances[t[i]][t[i+1]]

    result = max(r, result)


print(f'Result: {result}')