import os
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    lines = [line.strip() for line in f.readlines()]

def next_round(ms, g):
    new_ranges = []
    for dst, src, r in g:
        to_remove = []
        to_add = []
        for i, (s, e, o) in enumerate(ms):
            n_src = src - o
            if e > n_src and s < n_src + r:
                n_s = max(s, n_src)
                n_e = min(e, n_src + r)
                n_o = dst - n_src
                new_ranges.append((n_s, n_e, n_o))
                to_remove.append(i)
                to_add.append((s, n_s, o))
                to_add.append((n_e, e, o))
        for i in to_remove[::-1]:
            del ms[i]
        for t in to_add:
            if t[1] > t[0]:
                ms.append(t)
    return ms + new_ranges

nums = [int(i) for i in lines[0].split(": ")[1].split()]
seeds = []
m = 0
for i in range(0, len(nums), 2):
    m = max(m, nums[i] + nums[i + 1])
    seeds.append((nums[i], nums[i] + nums[i + 1]))


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
        m = max(m, temp[-1][0] + temp[-1][2], temp[-1][1] + temp[-1][2])

groups.append(temp)

mappings = [(0, m, 0)]

for group in groups:
    mappings = next_round(mappings, group)

result = 10e12
for start, end in seeds:
    for s, e, o in mappings:
        if e > start and s < end:
            result = min(result, max(s, start) + o)


print(f"Result: {result}")
