import string

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

result = 0

for line in lines:
    l = len(line) // 2
    a,b = line[:l],line[l:]

    for c in set(a).intersection(set(b)):
        result += string.ascii_letters.index(c) + 1

print(f'Result: {result}')
