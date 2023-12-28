import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def solve(lines):
    start = (1,0)
    end = (len(lines[0]) - 2, len(lines) - 1)

    graph = {}
    q = [(start, start, (0, 0), 0)]
    # First DFS to create graph just of junctions
    while len(q) > 0:
        pos, last_pos, last_dir, weight = q.pop()
        x, y = pos
        
        options = []
        for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx <= len(lines[0]) - 1 and ny >= 0 and ny <= len(lines) - 1 and lines[ny][nx] != "#":
                options.append((dx, dy))
        
        if len(options) != 2 and pos != start:
            # Create a node
            if last_pos not in graph:
                graph[last_pos] = set()
            graph[last_pos].add((x, y, weight))
            if pos not in graph:
                graph[pos] = set()
            graph[pos].add((*last_pos, weight))
            last_pos = pos
            weight = 0

            if len(options) > 2 and len(graph[pos]) == len(options):
                continue

        weight += 1

        for option in options:
            if option[0] == -last_dir[0] and option[1] == -last_dir[1]:
                continue # Cannot go back on ourselves
            q.append(((x + option[0], y + option[1]), last_pos, option, weight))

    best = 0
    q = [(start, set(), 0)]
    while len(q) > 0:
        pos, visited, cost = q.pop()

        if pos == end:
            best = max(best, cost)
            continue

        if pos in visited:
            continue
    
        visited.add(pos)

        for nx, ny, w in graph[pos]:
            new_pos = nx, ny
            if new_pos in visited:
                continue
            q.append((new_pos, visited.copy(), cost + w))

    return best


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
