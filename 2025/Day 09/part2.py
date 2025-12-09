import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

from bisect import bisect_left

############################################################
# Main solution code here

def solve(lines):
    points = []
    xs = set()
    ys = set()
    for i, line in enumerate(lines):
        x,y = [int(v) for v in line.split(",")]
        points.append((x,y))
        xs.add(x)
        ys.add(y)

    l_xs = list(xs)
    l_ys = list(ys)

    l_xs.sort()
    l_ys.sort()

    mapped_points = []
    hl = []
    vl = []
    last_x = l_xs.index(points[-1][0])
    last_y = l_ys.index(points[-1][1])
    for x, y in points:
        nx = l_xs.index(x)
        ny = l_ys.index(y)
        mapped_points.append((nx,ny))
        if nx == last_x:
            if last_y < ny:
                vl.append((nx, last_y, ny))
            else:
                vl.append((nx, ny, last_y))
        elif ny == last_y:
            if last_x < nx:
                hl.append((ny, last_x, nx))
            else:
                hl.append((ny, nx, last_x))
        last_x = nx
        last_y = ny

    hl.sort()
    vl.sort()

    def inside(x,y):
        # Count winding from ray going right
        idx = bisect_left(hl, (y,0,0))
        while idx < len(vl):
            ly, x1, x2 = hl[idx]
            if ly == y and x1 <= x <= x2:
                return True # It lies on a line or corner
            elif ly != y:
                break
            idx += 1
        idx = bisect_left(vl, (x,0,0))
        _inside = False
        while idx < len(vl):
            lx, y1, y2 = vl[idx]
            if lx == x and y1 <= y <= y2:
                return True # It lies on a line or corner
            elif y1 <= y < y2:
                _inside = not _inside
            idx += 1
        return _inside

    grid = [[inside(x,y) for y in range(len(l_ys))] for x in range(len(l_xs))]
    
    max_area = 0
    for i in range(len(mapped_points)):
        x1, y1 = mapped_points[i]
        for j in range(i+1, len(mapped_points)):
            x2, y2 = mapped_points[j]
            lx, ux = (x1, x2) if x1 < x2 else (x2, x1)
            ly, uy = (y1, y2) if y1 < y2 else (y2, y1)
            area = (l_xs[ux] - l_xs[lx] + 1) * (l_ys[uy] - l_ys[ly] + 1)
            if area > max_area:
                # If all of perimeter is inside, it's ok
                okay = True
                for x in range(lx, ux+1):
                    okay = okay and grid[x][ly]
                    okay = okay and grid[x][uy]
                    if not okay: break
                for y in range(ly, uy+1):
                    okay = okay and grid[lx][y]
                    okay = okay and grid[ux][y]
                    if not okay: break
                if okay:
                    max_area = area
    return max_area

############################################################
# Boilerplate

with open(os.path.join(SCRIPT_PATH, "sample.txt")) as f:
    sample = [line.strip() for line in f.readlines()]

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    puzzle = [line.strip() for line in f.readlines()]

UNITS = ["s", "ms", "μs"]

SAMPLE_START = time()
sample_result = solve(sample)
time_taken = time() - SAMPLE_START

unit_idx = 0
while time_taken < 1 and unit_idx < len(UNITS) - 1:
    time_taken *= 1000
    unit_idx += 1

print("Sample:")
print(f"Time: {time_taken:.2f}{UNITS[unit_idx]}")
print(f"Result: {sample_result}")
print()

PUZZLE_START = time()
puzzle_result = solve(puzzle)
time_taken = time() - PUZZLE_START

unit_idx = 0
while time_taken < 1 and unit_idx < len(UNITS) - 1:
    time_taken *= 1000
    unit_idx += 1

print("Puzzle:")
print(f"Time: {time_taken:.2f}{UNITS[unit_idx]}")
print(f"Result: {puzzle_result}")
