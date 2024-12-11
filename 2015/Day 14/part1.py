import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def get_distance_at_time(speed, fly_time, rest_time, target_time):
    cycle_time = fly_time + rest_time
    cycle_distance = fly_time * speed

    full_cycles = target_time // cycle_time
    remainder_time = target_time % cycle_time

    return full_cycles * cycle_distance + min(fly_time, remainder_time) * speed

def solve(lines):
    TARGET_TIME = 2503
    reindeer = []
    for line in lines:
        line = line.split(" ")
        name = line[0]
        speed = int(line[3])
        fly_time = int(line[6])
        rest_time = int(line[13])

        reindeer.append((name, get_distance_at_time(speed=speed, fly_time=fly_time, rest_time=rest_time, target_time=TARGET_TIME)))

    return max(reindeer, key=lambda a: a[1])[1]

############################################################
# Boilerplate

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    puzzle = [line.strip() for line in f.readlines()]

UNITS = ["s", "ms", "μs"]

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
