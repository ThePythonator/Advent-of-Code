# Tried: 173074 (too high), 123046 (correct)

digits = '0123456789'

with open('input.txt') as f:
    lines = [line.strip('\n') for line in f.readlines()]

_lines = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5""".split('\n')

path = []
i = 0
t = ''
while i < len(lines[-1]):
    c = lines[-1][i]
    
    if c in 'RL':
        path.append(int(t))
        path.append(c)
        t = ''
    else:
        t += c

    i += 1

grid = lines[:-2]

if c not in 'RL':
    path.append(int(t))

def add(x, y):
    return [x[i] + y[i] for i in range(min(len(x), len(y)))]

def minus(x, y):
    return [x[i] - y[i] for i in range(min(len(x), len(y)))]

def look(v):
    return ' ' if v[1] >= len(grid) or v[1] < 0 or v[0] >= len(grid[v[1]]) or v[0] < 0 else grid[v[1]][v[0]]

def look_xy(x, y):
    return grid[y][x]
    
def next_pos(p, d):
    # Assumes d only moves p by one square up/down/left/right
    n = add(p, d)
    if look(n) == ' ':
        n = p
        while look(n) != ' ':
            n = minus(n, d)

        n = add(n, d)
    return n

def get_dir(facing):
    if facing == 0:
        return [1, 0]
    elif facing == 1:
        return [0, 1]
    elif facing == 2:
        return [-1, 0]
    elif facing == 3:
        return [0, -1]

pos = [0, 0]
while look(pos) != '.':
    pos[0] += 1

facing = 0
for item in path:
    if item == 'L':
        facing -= 1
        facing %= 4
    elif item == 'R':
        facing += 1
        facing %= 4
    else:
        d = get_dir(facing)
        last = pos
        for i in range(item):
            p = next_pos(last, d)
            if look(p) != '.':
                p = last
                break
            last = p
        pos = p.copy()

result = (pos[1] + 1) * 1000 + (pos[0] + 1) * 4 + facing

print(f'Result: {result}')
