def product(args):
    if len(args) == 0:
        return 0
    else:
        total = 1
        for arg in args:
            total *= arg
        return total

with open('in.txt') as f:
    lines = [line.strip() for line in f.readlines()]

totalTrees = []

moves = [
    [1,1],
    [3,1],
    [5,1],
    [7,1],
    [1,2]
]

for move in moves:
    total = 0
    pos = [0,0]

    while pos[1] < len(lines):
        
        c = lines[pos[1]][pos[0]]


        if c == '#':
            total += 1

        pos[0] += move[0]
        pos[1] += move[1]
        pos[0] %= len(lines[0])

    totalTrees.append(total)

result = product(totalTrees)
print(result)
