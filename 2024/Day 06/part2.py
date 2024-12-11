import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def get_visited(sx, sy, lines):
    x, y = sx, sy
    dx, dy = 0, -1
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "^":
                x, y = j, i
    visited = set()
    visited_corners = set()
    guard_on_map = True
    while guard_on_map:
        while guard_on_map and lines[y][x] != "#":
            visited.add((x,y))
            x += dx
            y += dy
            guard_on_map = x >= 0 and x < len(lines[0]) and y >= 0 and y < len(lines)
        x -= dx
        y -= dy
        if guard_on_map:
            if (x,y,dx,dy) in visited_corners:
                # Will just continue in a loop
                return visited, True
            visited_corners.add((x,y,dx,dy))
            # Rotate clockwise
            if dx == 0:
                dx = -dy
                dy = 0
            else:
                dy = dx
                dx = 0
    return visited, False

def solve(lines):
    sx = sy = None
    dx, dy = 0, -1
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "^":
                sx, sy = j, i
    visited, _ = get_visited(sx, sy, lines)
    # It only make sense to place blocks in reachable places
    result = 0
    for vx, vy in visited:
        # Attempt to place a block here
        modified_lines = lines.copy()
        modified_lines[vy] = modified_lines[vy][:vx] + "#" + modified_lines[vy][vx+1:]
        _, looped = get_visited(sx, sy, modified_lines)
        if looped:
            result += 1
    
    return result


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
