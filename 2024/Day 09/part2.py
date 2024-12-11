import os
from time import time
import heapq
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def solve(lines):
    result = 0
    idx = 0
    fidx = 0
    frees = [] # (start, len) pairs
    files = [] # (start, len, id) triples
    final_order = []
    for i, c in enumerate(lines[0]):
        l = int(c)
        if i % 2 == 1:
            # Free space
            heapq.heappush(frees, (idx, l))
            final_order.extend([None] * l)
        else:
            files.append((idx, l, fidx))
            final_order.extend([fidx] * l)
            fidx += 1
        idx += l
    for s, l, i in files[::-1]:
        # print(f"{i}: s={s}, l={l}")
        # print("".join(str(c) if c is not None else "." for c in final_order))
        spares = []
        fs, fl = heapq.heappop(frees)
        success = True
        while fl < l:
            # Not enough space
            spares.append((fs, fl))
            if len(frees) > 0:
                fs, fl = heapq.heappop(frees)
            else:
                success = False
                break
        if success:
            if fs < s:
                # Don't move stuff later, only earlier
                for fi, fr in zip(range(s, s + l), range(fs, fs + fl)):
                    final_order[fr] = final_order[fi]
                    final_order[fi] = None
                heapq.heappush(frees, (fs+l, fl-l))
        for fs, fl in spares:
            heapq.heappush(frees, (fs, fl))
    for i, c in enumerate(final_order):
        if c is not None:
            result += i * c
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
