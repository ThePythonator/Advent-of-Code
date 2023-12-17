import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

import heapq

def create_heuristic_lookup(lines):
    w = len(lines[0])
    h = len(lines)
    global lookup
    lookup = {}
    q = [(0,(w-1,h-1))]
    while len(q) > 0:
        cost, pos = node = min(q)
        q.remove(node)
        new_cost = cost + int(lines[pos[1]][pos[0]])

        if pos not in lookup or lookup[pos] > cost:
            lookup[pos] = cost
        else:
            continue

        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            new_pos = (pos[0]+dx, pos[1]+dy)
            if new_pos[0] < 0 or new_pos[0] >= w or new_pos[1] < 0 or new_pos[1] >= h:
                continue
            q.append((new_cost, new_pos))

def solve(lines):
    w = len(lines[0])
    h = len(lines)
    create_heuristic_lookup(lines)
    q = [
        (0,0,0,(0,0),(1,0)),
        (0,0,0,(0,0),(0,1))
    ]
    visited = set()

    while len(q) > 0:
        _, cost, straight_line, pos, last_dir = heapq.heappop(q)
        
        if (pos, straight_line, last_dir) in visited:
            continue

        visited.add((pos, straight_line, last_dir))

        if pos == (w-1, h-1) and straight_line >= 4:
            return cost

        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            if last_dir[0] == -dx and last_dir[1] == -dy:
                continue
            if straight_line < 4 and (dx,dy) != last_dir:
                continue
            new_straight_line = 1
            if last_dir[0] == dx and last_dir[1] == dy:
                new_straight_line = straight_line + 1
                if straight_line == 10:
                    continue
            new_pos = (pos[0]+dx, pos[1]+dy)
            if new_pos[0] < 0 or new_pos[0] >= w or new_pos[1] < 0 or new_pos[1] >= h:
                continue
            new_cost = cost + int(lines[new_pos[1]][new_pos[0]])
            if (new_pos, new_straight_line, (dx,dy)) not in visited:
                # h_val = new_cost + w - 1 - new_pos[0] + h - 1 - new_pos[1] # worse heuristic (~4s)- but no need to preprocess
                h_val = new_cost + lookup[new_pos] # better heuristic (~2s), but preprocessing takes ~2s
                heapq.heappush(q, (h_val, new_cost, new_straight_line, new_pos, (dx,dy)))

    return -1

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
