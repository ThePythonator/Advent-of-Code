with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

elves = [0]

for line in lines:
    if line != '':
        elves[-1] += int(line)

    else:
        elves.append(0)

total = 0

for i in range(3):
    m = max(elves)
    elves.remove(m)
    total += m

print(f'Result: {total}')
