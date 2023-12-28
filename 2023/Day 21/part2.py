import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

from itertools import product

def plots_reachable(lines, steps, x, y, target=None, wrap=False):
    initial_steps = steps
    distances = {}
    totals = [0,0]
    visited = [set(), set()]
    q = [(steps, x, y)]
    while len(q) > 0:
        steps, x, y = q.pop(0)
        if (x, y) == target:
            return initial_steps - steps
        parity = (steps + 1) % 2
        for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx, ny = x + dx, y + dy
            if wrap:
                mx = nx % len(lines[0])
                my = ny % len(lines)
            else:
                mx, my = nx, ny
                if mx < 0 or mx >= len(lines[0]) or my < 0 or my >= len(lines):
                    continue
            if lines[my][mx] != "#" and (nx,ny) not in visited[parity]:
                visited[parity].add((nx,ny))
                totals[parity] += 1
                if steps > 1:
                    q.append((steps - 1, nx, ny))
        distances[initial_steps - steps + 1] = totals[parity]
    return sorted(distances.items())

def solve(lines, steps):
    w = len(lines[0])
    h = len(lines)

    start = (0, 0)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "S":
                start = (j, i)

    period = w
    assert w == h

    sequence = plots_reachable(lines, max(100, period * 3), *start, wrap=True)
    sequences = {i : [] for i in range(period)}
    for i in range(len(sequence)):
        sequences[i % period].append(sequence[i][1])
    
    first_differences = {}
    for i, seq in sequences.items():
        first_differences[i] = [seq[j+1] - seq[j] for j in range(len(seq) - 1)]
        
    second_differences = {}
    for i, seq in first_differences.items():
        second_differences[i] = [seq[j+1] - seq[j] for j in range(len(seq) - 1)]

    formulae = {}
    for i, seq in first_differences.items():
        a = second_differences[i][-1] / 2
        b = first_differences[i][-2] - 3 * a
        c = sequences[i][-3] - a - b
        x_offset = len(sequences[i]) - 3 - 1
        formulae[i] = (a,b,c,x_offset)

    # k = 1
    # print(sequences[k])
    # print(first_differences[k])
    # print(second_differences[k])
    # print(formulae[k])

    steps -= 1

    a,b,c,x_offset = formulae[steps % period]
    x = steps // period - x_offset
    result = a * x ** 2 + b * x + c

    # print()
    # print(x, steps % period, steps // period)
    # input()

    return int(result)


############################################################
# Boilerplate

with open(os.path.join(SCRIPT_PATH, "sample.txt")) as f:
    sample = [line.strip() for line in f.readlines()]

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    puzzle = [line.strip() for line in f.readlines()]

UNITS = ["s", "ms", "μs"]

SAMPLE_START = time()
sample_result = solve(sample, 5000)
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
puzzle_result = solve(puzzle, 26501365)
time_taken = time() - PUZZLE_START

unit_idx = 0
while time_taken < 1 and unit_idx < len(UNITS) - 1:
    time_taken *= 1000
    unit_idx += 1

print("Puzzle:")
print(f"Time: {time_taken:.2f}{UNITS[unit_idx]}")
print(f"Result: {puzzle_result}")
