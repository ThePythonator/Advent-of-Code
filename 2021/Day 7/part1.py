with open('input.txt') as f:
    crabs = [int(c) for c in f.readlines()[0].split(',')]

def count(i, crabs):
    total = 0
    for c in crabs:
        total += abs(c - i)

    return total

m = 999999999
for i in range(min(crabs), max(crabs)+1):
    m = min(m, count(i, crabs))

print(f'Results: {m}')
