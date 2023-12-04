n = 1321131112

n = str(n)

for i in range(50):
    t = 0
    l = n[0]
    r = ''
    for c in n:
        if c != l:
            r += str(t) + l
            l = c
            t = 0
        t += 1

    r += str(t) + c

    n = r

result = len(n)

print(f'Result: {result}')