with open('input.txt') as f:
    lines = [line.strip().split(' ') for line in f.readlines()]

depth = 0
dist = 0
aim = 0
for item in lines:
    cmd = item[0]
    amt = int(item[1])

    if cmd == 'forward':
        dist += amt
        depth += aim * amt
    elif cmd == 'down':
        aim += amt
    elif cmd == 'up':
        aim -= amt

print(f'Depth: {depth}, dist: {dist}')
print(f'Result: {depth*dist}')