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

for pos in positions:
    x,y,z = pos

    # Check for an adjacent cubes
    result += 6 - adj(x,y,z)

print(f'Result: {result}')
