s = 'vzbxkghb'
# s = 'ghijklmn'

a = 'abcdefghijklmnopqrstuvwxyz'

def inc_pass(p):
    s = ''
    carry = True
    for j in range(len(p)):
        c = p[-1-j]
        if carry:
            i = a.index(c) + 1

            if i > 25:
                i = 0
                carry = True
            
            else:
                carry = False
            
            c = a[i]
        
        s = c + s

    return s

running = True
while running:
    s = inc_pass(s)

    # if s[4:] == 'aaaa': print(s)

    if 'i' in s or 'o' in s or 'l' in s:
        continue

    triple = False
    for i in range(len(s) - 2):
        if a.index(s[i]) + 2 == a.index(s[i+1]) + 1 == a.index(s[i+2]):
            triple = True

    if not triple:
        continue
    
    doubles = 0

    i = 0
    while i < len(s) - 1:
        if s[i] == s[i+1]:
            doubles += 1
            i += 1
        i += 1
    
    if doubles < 2:
        continue

    result = s
    break

print(f'Result: {result}')