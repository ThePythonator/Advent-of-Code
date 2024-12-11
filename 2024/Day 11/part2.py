import os
from time import time
from functools import cache
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

@cache
def get_new_stones(stone):
    if stone == 0:
        return [1]
    str_stone = str(stone)
    str_len = len(str_stone)
    if str_len % 2 == 0:
        half = str_len // 2
        return [int(str_stone[:half]), int(str_stone[half:])]
    else:
        return [stone * 2024]
    
@cache
def get_new_stones_n_ahead(s, n):
    stones = [s]
    for _ in range(n):
        new_stones = []
        for stone in stones:
            new_stones.extend(get_new_stones(stone))
        stones = new_stones
    return stones

def solve(lines):
    stones = {}
    for i in lines[0].split():
        stone = int(i)
        if stone not in stones:
            stones[stone] = 1
        else:
            stones[stone] += 1
    for i in range(75):
        new_stones = {} # Keep tally of each
        for stone, n in stones.items():
            for ns in get_new_stones(stone):
                if ns not in new_stones:
                    new_stones[ns] = n
                else:
                    new_stones[ns] += n
        stones = new_stones
        # print(len(stones), sum(v for v in stones.values()))
    return sum(v for v in stones.values())


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
