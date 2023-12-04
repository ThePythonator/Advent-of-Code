import os
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    lines = [line.strip() for line in f.readlines()]

copies = [1]*len(lines)
result = 0
for i, line in enumerate(lines):
    winning, nums = [l.split(" ") for l in line.replace("  ", " ").split(": ")[1].split(" | ")]
    score = 0
    for w in winning:
        if w in nums:
            score += 1
            copies[i + score] += copies[i]
    result += copies[i]

print(f'Result: {result}')
