import os, itertools
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    lines = [line.strip() for line in f.readlines()]

def generate(s):
    return itertools.product(*[".#" if c == "?" else c for c in s])

def is_valid(option, nums):
    groups = [sum(1 for _ in v) for k, v in itertools.groupby(option) if k == "#"]
    return groups == nums

result = 0
for i, line in enumerate(lines):
    nums = [int(z) for z in line.split(" ")[1].split(",")]
    letters = line.split(" ")[0]
    possibilities = generate(letters)
    for possibility in possibilities:
        if is_valid(possibility, nums):
            result += 1

print(f"Result: {result}")
