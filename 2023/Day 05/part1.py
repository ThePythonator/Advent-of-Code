import os
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    lines = [line.strip() for line in f.readlines()]

seeds = [[int(i)] for i in lines[0].split(": ")[1].split()]

groups = []
temp = []
for line in lines[2:]:
    if "map" in line:
        continue
    elif line == "":
        groups.append(temp)
        temp = []
    else:
        temp.append([int(i) for i in line.split()])

groups.append(temp)

result = 0
for i, group in enumerate(groups):
    for line in group:
        dst_start, src_start, r = line
        for s in seeds:
            if s[i] >= src_start and s[i] < src_start + r:
                s.append(s[-1] - src_start + dst_start)
    for s in seeds:
        if len(s) < i + 2:
            s.append(s[-1])

result = 10e12
for s in seeds:
    result = min(result, s[-1])

print(f"Result: {result}")
