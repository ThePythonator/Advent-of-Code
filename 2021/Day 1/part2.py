with open('input.txt') as f:
    lines = [int(line.strip()) for line in f.readlines()]

total = 0
last = sum(lines[:3])
for i in range(len(lines) - 3):
    this = last + lines[i+3] - lines[i]
    if this > last: total += 1
    last = this

print(f'Total: {total}')
