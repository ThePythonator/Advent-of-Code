import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def intersecting(l, r, lower_bricks):
    (lx,ly,lz), (rx,ry,rz) = l, r
    indicies = []
    for i, ((ax,ay,az), (bx,by,bz)) in enumerate(lower_bricks):
        if (lx <= bx and rx >= ax and
            ly <= by and ry >= ay and 
            lz <= bz and rz >= az):
            indicies.append(i)
    return indicies


def solve(lines):
    bricks = []
    for i, line in enumerate(lines):
        bricks.append(list(tuple(int(i) for i in p.split(",")) for p in line.split("~")))

    bricks.sort(key=lambda b: (b[0][2], b[1][2]-b[0][2]))

    # Sorted in z-order, (for the same z value, thinner bricks are earlier)
    highest_z = 1
    dependencies = []
    for i in range(len(bricks)):
        (lx,ly,lz), (rx,ry,rz) = bricks[i]

        assert lx <= rx
        assert ly <= ry
        assert lz <= rz

        dz = lz - highest_z
        lz -= dz
        rz -= dz

        indicies = intersecting((lx,ly,lz), (rx,ry,rz), bricks[:i])
        while len(indicies) == 0 and lz > 0:
            lz -= 1
            rz -= 1
            indicies = intersecting((lx,ly,lz), (rx,ry,rz), bricks[:i])

        dependencies.append(indicies)

        lz += 1
        rz += 1
        
        bricks[i] = [(lx,ly,lz),(rx,ry,rz)]

        highest_z = max(highest_z, rz)

    result = len(bricks) - len(set(d[0] for d in dependencies if len(d) == 1))
    return result

############################################################
# Boilerplate

with open(os.path.join(SCRIPT_PATH, "sample.txt")) as f:
    sample = [line.strip() for line in f.readlines()]

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    puzzle = [line.strip() for line in f.readlines()]

SAMPLE_START = time()
sample_result = solve(sample)
print("Sample:")
print(f"Time: {time() - SAMPLE_START}")
print(f"Result: {sample_result}")
print()

PUZZLE_START = time()
puzzle_result = solve(puzzle)
print("Puzzle:")
print(f"Time: {time() - PUZZLE_START}")
print(f"Result: {puzzle_result}")
