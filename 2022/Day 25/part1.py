with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

_lines = """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122""".split('\n')

def decrypt(s):
    d = 0
    v = 1
    for c in s[::-1]:
        if c in '012':
            i = int(c)
        elif c == '-':
            i = -1
        else:
            i = -2
        d += v * i
        v *= 5
    return d

def encrypt(d):
    s = ''
    v = 1
    t = 2
    while t < d:
        v *= 5
        t += v * 2
    ended = False
    while not ended:
        if v == 1:
            ended = True
        u = t
        for i in range(2,-3,-1):
            u -= v
            if u < d:
                break
        t -= v * 2
        d -= v * i
        s += str(i) if i >= 0 else '-' if i == -1 else '='
        v /= 5
    return s

t = sum([decrypt(line) for line in lines])

result = encrypt(t)

print(f'Result: {result}')
