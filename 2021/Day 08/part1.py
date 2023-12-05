ONE = 2
FOUR = 4
SEVEN = 3
EIGHT = 7

OFSE = [ONE, FOUR, SEVEN, EIGHT]

def count_ofse(data):
    total = 0
    for item in data:
        if len(item) in OFSE:
            total += 1

    return total

with open('input.txt') as f:
    lines = [line.strip().split(' | ') for line in f.readlines()]

data = [[item.split(' ') for item in line] for line in lines]

total = 0
for line in data:
    total += count_ofse(line[1])

print(f'Result: {total}')
