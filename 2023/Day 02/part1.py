import os
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    lines = [line.strip() for line in f.readlines()]

def possible(line):
    subsets = line.split(": ")[1].split("; ")
    for subset in subsets:
        pairs = {l.split(" ")[1]: int(l.split(" ")[0]) for l in subset.split(", ")}
        r = pairs.get("red", 0)
        g = pairs.get("green", 0)
        b = pairs.get("blue", 0)

        if r > 12 or g > 13 or b > 14:
            return False
    
    return True

result = 0
for i, line in enumerate(lines, 1):
    if possible(line):
        result += i

print(f'Result: {result}')
