# Guessed: -341, -3799, 872 (correct)

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

_lines = """1
2
-3
3
-2
0
4""".split('\n')

values = [int(line) for line in lines]

new_values = []
rpts = {}

for v in values:
    if v not in rpts.keys():
        rpts[v] = 0

    new_values.append((v, rpts[v]))
    rpts[v] += 1

original_order = new_values.copy()

for t in original_order:
    o,c = t
    i = new_values.index(t)
    new_values.pop(i)
    i += o - 1
    i %= len(new_values)
    new_values.insert(i + 1, o)
    # input(len(values))
    # input(values[0])

j = new_values.index(0)

coord = [new_values[(j + i) % len(new_values)] for i in range(1000, 4000, 1000)]

result = sum(coord)
# print(coord)

# print(j, [(j + i) % len(values) for i in range(1000, 4000, 1000)])

print(f'Result: {result}')
