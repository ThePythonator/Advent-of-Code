import os, math
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    lines = [line.strip() for line in f.readlines()]

t = int(lines[0].split(": ")[1].replace(" ", ""))
d = int(lines[1].split(": ")[1].replace(" ", ""))

results = []
a = t / 2
b = math.sqrt(((t ** 2) / 4) - d)
x1 = a + b
x2 = a - b

if int(x1) == x1:
    x1 -= 0.1
if int(x2) == x2:
    x2 += 0.1

result = 1 + math.floor(x1) - math.ceil(x2)

print(f"Result: {result}")
