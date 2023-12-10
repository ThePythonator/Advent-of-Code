import os
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    lines = [line.strip() for line in f.readlines()]

def get_diff(seq):
    diff = []
    for i in range(len(seq) - 1):
        diff.append(seq[i + 1] - seq[i])
    return diff

def extrapolate(seq):
    diffs = [get_diff(seq)]
    while any(d != 0 for d in diffs[-1]):
        diffs.append(get_diff(diffs[-1]))
    # Last diff is all zeros
    diffs[-1].append(0)
    for i in range(len(diffs) - 2, -1, -1):
        diffs[i].append(diffs[i][-1] + diffs[i + 1][-1])
    return seq[-1] + diffs[0][-1]

result = 0
for i, line in enumerate(lines):
    result += extrapolate([int(i) for i in line.split()])

print(f"Result: {result}")
