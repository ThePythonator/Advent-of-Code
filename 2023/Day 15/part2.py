import os
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    lines = [line.strip() for line in f.readlines()]

def hash(s):
    v = 0
    for c in s:
        v += ord(c)
        v *= 17
        v %= 256
    return v

boxes = [[] for _ in range(256)]

for i, line in enumerate(lines[0].split(",")):
    if "=" in line:
        label = line[:-2]
        box = hash(label)
        n = int(line[-1])
        swapped = False
        for j, l in enumerate(boxes[box]):
            if l[0] == label:
                l[1] = n
                swapped = True
        if not swapped:
            boxes[box].append([label, n])
    else:
        label = line[:-1]
        box = hash(label)
        for j, l in enumerate(boxes[box]):
            if l[0] == label:
                del boxes[box][j]
                break


result = 0
for i, box in enumerate(boxes):
    for j, (l, n) in enumerate(box):
        result += (i + 1) * (j + 1) * n

print(f"Result: {result}")
