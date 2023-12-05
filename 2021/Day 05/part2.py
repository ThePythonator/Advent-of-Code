def plot_line(grid, start, end):
    # Assumes x1 = x2 or y1 = y2
    
    x = y = 0
    if start[0] == end[0]:
        x,y = start

        while end[1] != y:
            grid[y][x] += 1
            
            y += 1 if end[1] > y else -1

        grid[y][x] += 1

    elif start[1] == end[1]:
        x,y = start

        while end[0] != x:
            grid[y][x] += 1

            x += 1 if end[0] > x else -1

        grid[y][x] += 1

    else:
        # Assume diagonal
        x,y = start

        while end[0] != x:
            grid[y][x] += 1
            
            x += 1 if end[0] > x else -1
            y += 1 if end[1] > y else -1
            
        grid[y][x] += 1
        
    return grid

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

lines = [line.split(' -> ') for line in lines]
lines = [[[int(sub.split(',')[0]), int(sub.split(',')[1])] for sub in line] for line in lines]

m = 0
for line in lines:
    for sub in line:
        m = max(m, max(sub))

m += 1
        
grid = [[0] * m for i in range(m)]

for line in lines:
    grid = plot_line(grid, line[0], line[1])

count = 0
for row in grid:
    for item in row:
        if item >= 2:
            count += 1

print(f'Result: {count}')
