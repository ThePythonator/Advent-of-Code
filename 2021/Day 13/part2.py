def combine(a, b):
    n = []
    for i in range(max(len(a), len(b))):
        n.append('#' if a[i] == '#' or b[i] == '#' else '.')

    return n

def fold_grid(grid, fold):
    if fold[0] == 'x':
        for y in range(len(grid)):
            grid[y] = combine(grid[y][:fold[1]], grid[y][fold[1]+1:][::-1])
            
    elif fold[0] == 'y':
        s = len(grid)
        for y in range(fold[1]):
            grid[y] = combine(grid[y], grid[s-1-y])
        del grid[fold[1]:]

    return grid

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

i = 0
while lines[i] != '':
    i += 1

dots = [[int(dot.split(',')[0]), int(dot.split(',')[1])] for dot in lines[:i]]
folds = [fold.replace('fold along ','') for fold in lines[i+1:]]
folds = [[fold.split('=')[0], int(fold.split('=')[1])] for fold in folds]

max_x = max([dot[0] for dot in dots])+1
max_y = max([dot[1] for dot in dots])+1

grid = []
for i in range(max_y):
    grid.append(['.']*max_x)

for dot in dots:
    grid[dot[1]][dot[0]] = '#'

for fold in folds:
    grid = fold_grid(grid, fold)

c = 0
for line in grid:
    c += line.count('#')

print(f'Result: {c}')

for line in grid:
    print(''.join(line))


