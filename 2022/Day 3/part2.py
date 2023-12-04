with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

result = 0
for line in lines:
    x,y = [i for i in line.split(',')]
    a,b = [int(i) for i in x.split('-')]
    c,d = [int(i) for i in y.split('-')]

    if (b >= c and a <= d) or (d >= a and c <= b):
        result += 1

print(f'Result: {result}')
