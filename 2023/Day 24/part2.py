import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

import numpy as np

def intersects(a, b):
    # print(a,b)
    (x_a, y_a, _), (vx_a, vy_a, _) = a
    (x_b, y_b, _), (vx_b, vy_b, _) = b
    denom = vx_a * vy_b - vy_a * vx_b
    if denom == 0:
        return None
    t_2 = (vy_a * (x_b - x_a) - vx_a * (y_b - y_a)) / denom
    t_1 = (x_b - x_a + vx_b * t_2) / vx_a
    # print(t_1, t_2)
    if t_1 < 0 or t_2 < 0: return None
    x = x_a + vx_a * t_1
    y = y_a + vy_a * t_1
    _x = x_b + vx_b * t_2
    _y = y_b + vy_b * t_2 # This seems correct but x,y seems wrong???
    # print(x,y,_x,_y)
    # assert x == _x and y == _y
    return (_x,_y)

def solve(lines):
    hailstones = []
    for line in lines:
        pos, vel = [[int(i) for i in l.split(", ")] for l in line.split(" @ ")]
        hailstones.append((pos,vel))
    
    pairs = []
    for i in range(len(hailstones)):
        for j in range(i + 1, len(hailstones)):
            # Compare each pair
            pairs.append((hailstones[i], hailstones[j]))
    
    m = [[],[]]
    r = [[],[]]
    for a, b in pairs[:4]:
        for i in range(2):
            if i == 0:
                (x_a, y_a, _), (vx_a, vy_a, _) = a
                (x_b, y_b, _), (vx_b, vy_b, _) = b
            else:
                (x_a, _, y_a), (vx_a, _, vy_a) = a
                (x_b, _, y_b), (vx_b, _, vy_b) = b
            k = vx_a * y_a - x_a * vy_a + x_b * vy_b - vx_b * y_b
            alpha = vy_b - vy_a
            beta = vx_a - vx_b
            gamma = y_a - y_b
            delta = x_b - x_a
            r[i].append(k)
            m[i].append([alpha, beta, gamma, delta])

    xy_result, xz_result = [
        np.linalg.solve(np.array(m[i]), np.array(r[i])) for i in range(2)
    ]
    x, y = xy_result[:2]
    _x, z = xz_result[:2]
    assert round(x) == round(_x)
    x = round(x)
    y = round(y)
    z = round(z)

    result = x + y + z

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
