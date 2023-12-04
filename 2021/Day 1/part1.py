with open('input.txt') as f:
    lines = [int(line.strip()) for line in f.readlines()]

total = 0
last = lines[0]
for line in lines:
    if line > last: total += 1
    last = line

print(f'Total: {total}')
