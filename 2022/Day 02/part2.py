values = {'X':0,'Y':3,'Z':6}
scores = {'A':{'X':3,'Y':1,'Z':2},'B':{'X':1,'Y':2,'Z':3},'C':{'X':2,'Y':3,'Z':1}}

with open('input.txt') as f:
    lines = [line.strip().split(' ') for line in f.readlines()]

total = 0

for line in lines:
    total += values[line[1]] + scores[line[0]][line[1]]

print(f'Result: {total}')
