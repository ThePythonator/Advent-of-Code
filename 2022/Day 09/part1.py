with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

# lines = """R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2""".split('\n')

h = [0,0]
t = [0,0]
p = set()
for line in lines:
    m, a = line.split(' ')
    a = int(a)

    for i in range(a):
        if m == 'U':
            h[1] += 1
        elif m == 'D':
            h[1] -= 1
        elif m == 'L':
            h[0] += 1
        elif m == 'R':
            h[0] -= 1

        if h[0] > t[0] + 1:
            t[0] += 1
            t[1] = h[1]
        elif h[0] < t[0] - 1:
            t[0] -= 1
            t[1] = h[1]

        if h[1] > t[1] + 1:
            t[1] += 1
            t[0] = h[0]
        elif h[1] < t[1] - 1:
            t[1] -= 1
            t[0] = h[0]

        p.add(tuple(t))

result = len(p)

print(f'Result: {result}')
