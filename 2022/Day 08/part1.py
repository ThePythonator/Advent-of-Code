with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

result = (len(lines) + len(lines[0]) - 2) * 2

for i, line in enumerate(lines[1:-1]):
    for j, c in enumerate(line[1:-1]):
        ok = False

        temp_ok = True
        x = j+1
        while x > 0:
            if line[x-1] >= line[j+1]:
                temp_ok = False
                break
            x -= 1
        
        ok = ok or temp_ok

        temp_ok = True
        x = j+1
        while x < len(line) - 1:
            if line[x+1] >= line[j+1]:
                temp_ok = False
                break
            x += 1
        
        ok = ok or temp_ok

        temp_ok = True

        y = i+1
        while y > 0:
            if lines[y-1][j+1] >= lines[i+1][j+1]:
                temp_ok = False
                break
            y -= 1
        
        ok = ok or temp_ok

        temp_ok = True

        y = i+1
        
        while y < len(lines) - 1:
            if lines[y+1][j+1] >= lines[i+1][j+1]:
                temp_ok = False
                break
            y += 1
        
        ok = ok or temp_ok

        if ok: result += 1

print(f'Result: {result}')
