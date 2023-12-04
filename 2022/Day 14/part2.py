with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

def put(st, c, i):
    return st[:i] + c + st[i+1:]

def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0

# lines = """498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9""".split('\n')

s = ['+']

tl = [500,0]
src = tl.copy()

for line in lines:
    p = [[int(i) for i in l.split(',')] for l in line.split(' -> ')]

    for q in p:
        if q[0] < tl[0]:
            s = ['.'*(tl[0] - q[0]) + r for r in s]
            tl[0] = q[0]

        if 1 + q[0] > tl[0] + len(s[0]):
            s = [r + '.'*(1 + q[0] - tl[0] - len(s[0])) for r in s]

        while q[1] >= tl[1] + len(s):
            s.append('.'*len(s[0]))

    for j in range(1, len(p)):
        b = p[j-1]
        q = p[j]

        v = [q[0] - b[0], q[1] - b[1]]
        if v[0] != 0:
            c = abs(v[0])
            v[0] = sign(v[0])
        if v[1] != 0:
            c = abs(v[1])
            v[1] = sign(v[1])

        t = [b[0] - tl[0], b[1] - tl[1]]
        for i in range(c + 1):
            # print(s[t[1]])

            s[t[1]] = put(s[t[1]], '#', t[0])

            # print(s[t[1]], t[0])

            # input()

            t[0] += v[0]
            t[1] += v[1]

    # for r in s:
    #     print(r)

    # input()


s.append('.'*len(s[0]))
s.append('#'*len(s[0]))

result = 0

running = True
while running:
    sand_pos = [src[0] - tl[0], src[1] - tl[1]]
    moving = True

    while moving:
        if sand_pos[0] - 1 < 0:
            s = ['.'*(1 - sand_pos[0]) + r for r in s]
            tl[0] -= 1 - sand_pos[0]
            sand_pos[0] = 1

        if 2 + sand_pos[0] > len(s[0]):
            s = [r + '.'*(2 + sand_pos[0] - len(s[0])) for r in s]

        s[-1] = '#'*len(s[0])

        if s[sand_pos[1] + 1][sand_pos[0]] == '.':
            sand_pos[1] += 1

        elif s[sand_pos[1] + 1][sand_pos[0] - 1] == '.':
            sand_pos[1] += 1
            sand_pos[0] -= 1
        
        elif s[sand_pos[1] + 1][sand_pos[0] + 1] == '.':
            sand_pos[1] += 1
            sand_pos[0] += 1

        else:
            moving = False

    s[sand_pos[1]] = put(s[sand_pos[1]], 'o', sand_pos[0])
    result += 1

    if sand_pos[0] == src[0] - tl[0] and sand_pos[1] == src[1] - tl[1]:
        running = False

    # for r in s:
    #     print(r)
    # input()

print(f'Result: {result}')
