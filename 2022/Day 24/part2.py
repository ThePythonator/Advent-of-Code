import math,time

from functools import cache

offset_lookup = {
    '>':[1,0],
    'v':[0,1],
    '<':[-1,0],
    '^':[0,-1]
}

def add(a,b):
    return [a[0]+b[0],a[1]+b[1]]

@cache
def dist(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def move_blizzards(blizzards, true_dim):
    b_p = []
    for c,p in blizzards:
        x,y = add(p, offset_lookup[c])
        if x == 0:
            x = true_dim[0]
        elif x == true_dim[0] + 1:
            x = 1
        elif y == 0:
            y = true_dim[1]
        elif y == true_dim[1] + 1:
            y = 1
        b_p.append((c,(x,y)))
    return b_p

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

s = time.time()
_lines = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#""".split('\n')

# Initial setup

print('Starting lookup generation')

grid = lines

start = (1,0)
target = (len(grid[0])-2,len(grid)-1)

dim = [len(grid[0]), len(grid)]
true_dim = [dim[0]-2,dim[1]-2]
lcm = math.lcm(true_dim[0],true_dim[1])

blizzards = [(grid[y][x], (x,y)) for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] != '.' and grid[y][x] != '#']
blizzard_positions = []

for i in range(lcm):
    blizzards = move_blizzards(blizzards, true_dim)
    blizzard_positions.append(set(p for c,p in blizzards))

@cache
def valid_position(position, k):
    if position == start or position == target:
        return True
    if position not in blizzard_positions[k] and 1 <= position[0] <= true_dim[0] and 1 <= position[1] <= true_dim[1]:
        return True
    return False

print('Generated lookup')

def solve(begin, end, start_time):
    
    best = 9999
    
    q = [(start_time,begin)]

    seen = set()
    
    while len(q) > 0:
        state = q.pop()

        if state in seen:
            continue
        
        seen.add(state)

        time, pos = state

        if pos == end:
            best = min(best, time)
            continue
        elif dist(pos, end) + time >= best:
            continue
        elif time > 1000:
            continue

        i = time % lcm
        
        if tuple(pos) not in blizzard_positions[i]:
            q.append((time+1,pos))

        x,y = pos

        if valid_position((x-1,y), i):
            q.append((time+1,(x-1,y)))
        if valid_position((x,y-1), i):
            q.append((time+1,(x,y-1)))
        if valid_position((x+1,y), i):
            q.append((time+1,(x+1,y)))
        if valid_position((x,y+1), i):
            q.append((time+1,(x,y+1)))
    return best

result = solve(start, target, 0)
result = solve(target, start, result)
result = solve(start, target, result)

print(f'Result: {result}')
e = time.time()

# print(e-s)