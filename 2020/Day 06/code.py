with open('in.txt') as f:
    lines = [line.strip() for line in f.readlines()]+['']


total = 0
l = []
s = []
group = 0

for line in lines:
    if line == '':
        for c in s:
            if l.count(c) == group:
                total += 1
            
        l = []
        s = []
        group = 0
        
    else:
        group += 1
        for c in line:
            l.append(c)
            if c not in s:
                s.append(c)

print(total)
