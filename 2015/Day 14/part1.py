import os
INPUT_FILE = os.path.join(os.path.dirname(__file__), "input.txt")

def get_distance_at_time(speed, fly_time, rest_time, target_time):
    cycle_time = fly_time + rest_time
    cycle_distance = fly_time * speed

    full_cycles = target_time // cycle_time
    remainder_time = target_time % cycle_time

    return full_cycles * cycle_distance + min(fly_time, remainder_time) * speed


TARGET_TIME = 2503

reindeer = []

with open(INPUT_FILE) as f:
    for line in f.readlines():
        line = line.strip().split(" ")
        name = line[0]
        speed = int(line[3])
        fly_time = int(line[6])
        rest_time = int(line[13])

        reindeer.append((name, get_distance_at_time(speed=speed, fly_time=fly_time, rest_time=rest_time, target_time=TARGET_TIME)))

result = max(reindeer, key=lambda a: a[1])

print(f"Result: {result}")