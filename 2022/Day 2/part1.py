values = {'X':1,'Y':2,'Z':3}
scores = {'A':{'X':3,'Y':6,'Z':0},'B':{'X':0,'Y':3,'Z':6},'C':{'X':6,'Y':0,'Z':3}}

with open('input.txt') as f:
    lines = [line.strip().split(' ') for line in f.readlines()]

total = 0

for line in lines:
    total += values[line[1]] + scores[line[0]][line[1]]

print(f'Result: {total}')
