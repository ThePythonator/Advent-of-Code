with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

elves = [0]

for line in lines:
    if line != '':
        elves[-1] += int(line)

    else:
        elves.append(0)

print(f'Result: {max(elves)}')
