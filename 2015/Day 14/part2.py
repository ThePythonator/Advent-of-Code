import os
INPUT_FILE = os.path.join(os.path.dirname(__file__), "input.txt")


TARGET_TIME = 2503

reindeer = []

with open(INPUT_FILE) as f:
    for line in f.readlines():
        line = line.strip().split(" ")
        name = line[0]
        speed = int(line[3])
        fly_time = int(line[6])
        rest_time = int(line[13])

        reindeer.append((name, speed, fly_time, rest_time, fly_time, 0, 0)) # 5th item: flying timer, 6th item: resting timer, 7th item: points

for i in range(TARGET_TIME):
    for r in reindeer:
        pass # TODO

result = max(reindeer, key=lambda a: a[1])

print(f"Result: {result}")