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

def solve(lines, target_time):
    reindeer = {}
    scores = {}
    for line in lines:
        line = line.split(" ")
        name = line[0]
        speed = int(line[3])
        fly_time = int(line[6])
        rest_time = int(line[13])
        reindeer[name] = (speed, fly_time, rest_time)
        scores[name] = 0

    for t in range(1, target_time + 1):
        distances = []
        for name, (speed, fly_time, rest_time) in reindeer.items():
            dist = get_distance_at_time(speed=speed, fly_time=fly_time, rest_time=rest_time, target_time=t)
            distances.append((name, dist))
        best_dist = max(distances, key=lambda a: a[1])[1]
        for name, dist in distances:
            if dist == best_dist:
                scores[name] += 1
    return max(scores.items(), key=lambda a: a[1])[1]

############################################################
# Boilerplate

with open(os.path.join(SCRIPT_PATH, "sample.txt")) as f:
    sample = [line.strip() for line in f.readlines()]

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    puzzle = [line.strip() for line in f.readlines()]

UNITS = ["s", "ms", "μs"]

SAMPLE_START = time()
sample_result = solve(sample, 1000)
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
puzzle_result = solve(puzzle, 2503)
time_taken = time() - PUZZLE_START

unit_idx = 0
while time_taken < 1 and unit_idx < len(UNITS) - 1:
    time_taken *= 1000
    unit_idx += 1

print("Puzzle:")
print(f"Time: {time_taken:.2f}{UNITS[unit_idx]}")
print(f"Result: {puzzle_result}")
