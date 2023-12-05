with open('in.txt') as f:
    lines = [line.strip() for line in f.readlines()]

def attempt(lines):
    i = 0
    instructionsDone = []
    acc = 0
    while i not in instructionsDone and i < len(lines):
        instructionsDone.append(i)

        line = lines[i]

        ins,num = line.split(' ')
        num = int(num)

        if ins == 'nop':
            i += 1

        elif ins == 'acc':
            acc += num
            i += 1

        elif ins == 'jmp':
            i += num
            
    if i not in instructionsDone:
        return acc

    else:
        return None

##    if i in instructionsDone:
##        if ins == 'jmp':
##            i -= num
##            ins = 'nop'
##            
##        elif ins == 'nop':
##            i -= num
##            ins = 'jmp'
##
##        if ins == 'nop':
##            i += 1
##
##        elif ins == 'jmp':
##            i += num

for j in range(len(lines)):
    res = None
    c = lines.copy()
    if c[j][:3] == 'nop':
        c[j] = 'jmp' + c[j][3:]
        res = attempt(c)
    elif c[j][:3] == 'jmp':
        c[j] = 'nop' + c[j][3:]
        res = attempt(c)

    if res != None:
        print(res)
     
