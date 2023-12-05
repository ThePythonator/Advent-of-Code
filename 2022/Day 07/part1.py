import os

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

paths = {}

cwd = ''
for line in lines:
    s = line.split(' ')

    if s[0] == '$':
        if s[1] == 'cd':
            cwd = os.path.join(cwd, s[2])
            cwd = os.path.normpath(cwd)
            
    else:
        if s[0] != 'dir':
            paths[os.path.join(cwd, s[1])] = int(s[0])

dirs = {}

for p in paths.keys():
    d = os.path.dirname(p)

    while d != os.path.normpath('/'):

        if d in dirs.keys():
            dirs[d] += paths[p]

        else:
            dirs[d] = paths[p]

        d = os.path.normpath(os.path.join(d, '../'))

result = 0
for d in dirs.keys():
    if dirs[d] < 100000:
        result += dirs[d]

print(f'Result: {result}')
