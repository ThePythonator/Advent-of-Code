with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

result = 0

_lines = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5""".split('\n')

positions = set([tuple([int(a) for a in line.split(',')]) for line in lines])

boundaries = [[min([pos[i] - 1 for pos in positions]) for i in range(3)], [max([pos[i] for pos in positions]) for i in range(3)]]

outside_pos = tuple(boundaries[0])

def flood_fill(p):
    q = [p]

    mi_x, mi_y, mi_z = boundaries[0]
    ma_x, ma_y, ma_z = boundaries[1]

    k = []

    while len(q) > 0:
        n = q.pop(0)

        if n not in positions and n not in k:
            k.append(n)

            x,y,z = n

            if ma_x > x: q.append((x+1,y,z))
            if mi_x < x: q.append((x-1,y,z))
            if ma_y > y: q.append((x,y+1,z))
            if mi_y < y: q.append((x,y-1,z))
            if ma_z > z: q.append((x,y,z+1))
            if mi_z < z: q.append((x,y,z-1))

    return k

def adj(x,y,z):
    c = 0
    if (x+1,y,z) in positions:
        c += 1
    if (x,y+1,z) in positions:
        c += 1
    if (x,y,z+1) in positions:
        c += 1
    if (x-1,y,z) in positions:
        c += 1
    if (x,y-1,z) in positions:
        c += 1
    if (x,y,z-1) in positions:
        c += 1
    return c

temp_positions = list(positions)
avoid = []
valid = []
while len(temp_positions) > 0:
    x,y,z = temp_positions.pop(0)
    for _x,_y,_z in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
        v = (x+_x,y+_y,z+_z)
        if v not in positions and v not in avoid:
            temp = flood_fill(v)
            if outside_pos in temp:
                temp_positions = [_p for _p in temp_positions if _p not in temp]
                avoid += [_p for _p in temp if _p not in avoid]
                # print("outside, avoid len=",len(avoid))
            else:
                # print("valid")
                valid += [_v for _v in temp if _v not in valid]

    # print(len(temp_positions))

positions = set(list(positions) + valid)

for pos in positions:
    x,y,z = pos

    # Check for an adjacent cubes
    result += 6 - adj(x,y,z)

print(f'Result: {result}')
