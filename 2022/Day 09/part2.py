with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0

# lines = """R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20""".split('\n')

t = [[0,0] for i in range(10)]
p = set()
for line in lines:
    m, a = line.split(' ')
    a = int(a)

    for i in range(a):
        if m == 'U':
            t[0][1] += 1
        elif m == 'D':
            t[0][1] -= 1
        elif m == 'L':
            t[0][0] += 1
        elif m == 'R':
            t[0][0] -= 1

        for i in range(1, len(t)):
            if t[i-1][0] > t[i][0] + 1:
                t[i][0] += 1
                t[i][1] += sign(t[i-1][1] - t[i][1])
            elif t[i-1][0] < t[i][0] - 1:
                t[i][0] -= 1
                t[i][1] += sign(t[i-1][1] - t[i][1])

            if t[i-1][1] > t[i][1] + 1:
                t[i][1] += 1
                t[i][0] += sign(t[i-1][0] - t[i][0])
            elif t[i-1][1] < t[i][1] - 1:
                t[i][1] -= 1
                t[i][0] += sign(t[i-1][0] - t[i][0])

            p.add(tuple(t[-1]))

        # input(t)

        # z = ['.'*26]*21

        # for i, item in enumerate(t):
        #     z[15-item[1]] = z[15-item[1]][:item[0]+15-1] + str(i) + z[15-item[1]][item[0]+15:]

        # for line in z: print(line[::-1])

        # input()

result = len(p)

# z = ['.'*26]*21

# for i, item in enumerate(p):
#     z[15-item[1]] = z[15-item[1]][:item[0]+15-1] + '#' + z[15-item[1]][item[0]+15:]

# for line in z: print(line[::-1])

# input()

print(f'Result: {result}')
