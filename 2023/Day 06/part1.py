import os, math
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    lines = [line.strip() for line in f.readlines()]

times = [int(i) for i in lines[0].split(": ")[1].split()]
dists = [int(i) for i in lines[1].split(": ")[1].split()]

results = []
for t, d in zip(times, dists):
    a = t / 2
    b = math.sqrt(((t ** 2) / 4) - d)
    x1 = a + b
    x2 = a - b

    if int(x1) == x1:
        x1 -= 0.1
    if int(x2) == x2:
        x2 += 0.1

    n = 1 + math.floor(x1) - math.ceil(x2)

    results.append(n)

result = math.prod(results)
print(f"Result: {result}")
