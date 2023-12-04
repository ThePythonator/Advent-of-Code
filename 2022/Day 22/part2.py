# Tried: 129193 (too low)

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

SIZE = 50

def gen_face_lookup():
    f_l = {}
    c = 0
    for y in range(0, len(grid), SIZE):
        for x in range(0, len(grid[y]), SIZE):
            if look_xy(x, y) != ' ':
                # Allow lookups both ways
                f_l[(x//SIZE,y//SIZE)] = c
                f_l[c] = (x,y)
                c += 1
    return f_l

def gen_next_face_and_direction_lookup():
    # very VERY hacky
    # return {0:{0:(5,0),2:(2,3),3:(1,3)},1:{1:(4,1),2:(5,1),3:(0,3)},2:{1:(4,2),3:(0,2)},3:{0:(5,3)},4:{1:(1,1),2:(2,1)},5:{0:(0,0),1:(1,2),3:(3,0)}}
    return {
        0:{2:(3,2),3:(5,2)},
        1:{0:(4,0),1:(2,0),3:(5,1)},
        2:{0:(1,1),2:(3,3)},
        3:{2:(0,2),3:(2,2)},
        4:{0:(1,0),1:(5,0)},
        5:{0:(4,1),1:(1,3),2:(0,3)}
    }

def get_face(p):
    return face_lookup[(p[0]//SIZE,p[1]//SIZE)]

def get_next_face_and_facing(p, facing):
    f = get_face(p)
    r = next_face_and_direction_lookup[f][facing]
    return r[0], (r[1] + 2) % 4

def get_next_face_pos_and_dir(p, facing):
    n_f, n_d = get_next_face_and_facing(p, facing)
    # print(n_f, n_d)
    a = p[1] if facing & 1 == 0 else p[0]
    initial_index = a % SIZE
    # print(initial_index)
    swap = (facing in [0,3] and n_d in [1,2]) or (facing in [1,2] and n_d in [0,3])
    if swap:
        initial_index = SIZE - 1 - initial_index
        # print("SWAP")
    new_p = list(face_lookup[n_f])
    if n_d & 2 != 0:
        if n_d & 1 == 0:
            new_p[0] += SIZE - 1
        else:
            new_p[1] += SIZE - 1
    # print(*new_p,initial_index)
    if n_d & 1 == 1:
        new_p[0] += initial_index
    else:
        new_p[1] += initial_index
    return new_p, n_d
    
def next_pos(p, facing):
    # Assumes d only moves p by one square up/down/left/right
    d = get_dir(facing)
    n = add(p, d)
    if look(n) == ' ':
        n, f = get_next_face_pos_and_dir(p, facing)
        if look(n) != '.':
            n = p
        else:
            facing = f
    return n, facing

def get_dir(facing):
    if facing == 0:
        return [1, 0]
    elif facing == 1:
        return [0, 1]
    elif facing == 2:
        return [-1, 0]
    elif facing == 3:
        return [0, -1]


face_lookup = gen_face_lookup()
next_face_and_direction_lookup = gen_next_face_and_direction_lookup()

pos = [0, 0]
while look(pos) != '.':
    pos[0] += 1

facing = 0
for item in path:
    # print(item, pos, facing)
    # input()
    if item == 'L':
        facing -= 1
        facing %= 4
    elif item == 'R':
        facing += 1
        facing %= 4
    else:
        last = pos
        for i in range(item):
            p, n_f = next_pos(last, facing)
            if look(p) != '.':
                p = last
                break
            last = p
            facing = n_f
            # input(p)
        pos = p.copy()
        # print('face',get_face(pos),'facing',facing,'amt',item)
        # input(pos)

result = (pos[1] + 1) * 1000 + (pos[0] + 1) * 4 + facing

print(f'Result: {result}')
