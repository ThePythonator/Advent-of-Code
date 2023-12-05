with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

total = len(lines)
counts = [0] * len(lines[0])

for item in lines:
    for i, char in enumerate(item):
        if char == '1':
            counts[i] += 1


def rem(l, i, b):
    to_rem = []
    
    print(l, i, b)
    for item in l:
        if item[i] != b:
            to_rem.append(item)

    for item in to_rem:
        l.remove(item)

    return l

ox = lines.copy()
co = lines.copy()

o = ''
c = ''

i = 0

while True:
    i += 1

    if i == len(lines[0]): break

    c = 0
    for item in lines:
        if item[i] == '1':
            c += 1
    
    if c >= len(ox) / 2:
        # 1s for oxy
        if len(ox) > 1: ox = rem(ox, i, '1')
    else:
        # 0 for oxy
        if len(ox) > 1: ox = rem(ox, i, '0')
        
    if c >= len(co) / 2:
        if len(co) > 1: co = rem(co, i, '0')
    else:
        if len(co) > 1: co = rem(co, i, '1')

    if len(ox) == 1 and len(co) == 1:
        break;

o = ox[0]
c = co[0]
result = int(o, 2) * int(c, 2)

print(f'Final: {o}, {c}')
print(f'Result: {result}')
