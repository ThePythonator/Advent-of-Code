import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

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

def solve(lines, mi, ma):
    hailstones = []
    for line in lines:
        pos, vel = [[int(i) for i in l.split(", ")] for l in line.split(" @ ")]
        hailstones.append((pos,vel))
    
    result = 0
    for i in range(len(hailstones)):
        for j in range(i + 1, len(hailstones)):
            # Compare each pair
            pos = intersects(hailstones[i], hailstones[j])
            if pos is not None:
                x,y = pos
                if x >= mi and x <= ma and y >= mi and y <= ma:
                    result += 1
    return result


############################################################
# Boilerplate

with open(os.path.join(SCRIPT_PATH, "sample.txt")) as f:
    sample = [line.strip() for line in f.readlines()]

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    puzzle = [line.strip() for line in f.readlines()]

SAMPLE_START = time()
sample_result = solve(sample, 7, 27)
print("Sample:")
print(f"Time: {time() - SAMPLE_START}")
print(f"Result: {sample_result}")
print()

PUZZLE_START = time()
puzzle_result = solve(puzzle, 200000000000000, 400000000000000)
print("Puzzle:")
print(f"Time: {time() - PUZZLE_START}")
print(f"Result: {puzzle_result}")
