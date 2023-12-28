import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def solve(lines):
    start = (1,0)
    end = (len(lines[0]) - 2, len(lines) - 1)

    best = set()
    
    q = [(*start, set())]
    while len(q) > 0:
        x, y, visited = q.pop(0)
        if (x,y) in visited:
            continue
        if (x,y) == end:
            if len(visited) > len(best):
                best = visited
                continue
        visited.add((x,y))
        c = lines[y][x]
        if c == ">":
            q.append((x+1,y,visited))
        elif c == "<":
            q.append((x-1,y,visited))
        elif c == "v":
            q.append((x,y+1,visited))
        elif c == "^":
            q.append((x,y-1,visited))
        else:
            for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                nx, ny = x+dx, y+dy
                if (nx, ny) in visited or nx < 0 or nx >= len(lines[0]) or ny < 0 or ny >= len(lines):
                    continue
                if lines[ny][nx] != "#":
                    q.append((nx,ny,visited.copy()))

    result = len(best)
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
