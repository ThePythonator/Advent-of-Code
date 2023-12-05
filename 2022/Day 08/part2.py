with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

# lines = """30373
# 25512
# 65332
# 33549
# 35390""".split('\n')

result = 0

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        score = 1

        t = 0
        x = j
        while x > 0:
            t += 1
            if line[x-1] >= line[j]: break
            x -= 1
            
        score *= t
        t = 0
        x = j
        while x < len(line) - 1:
            t += 1
            if line[x+1] >= line[j]: break
            x += 1

        score *= t
        t = 0
        y = i
        while y > 0:
            t += 1
            if lines[y-1][j] >= lines[i][j]: break
            y -= 1

        score *= t
        t = 0
        y = i
        
        while y < len(lines) - 1:
            t += 1
            if lines[y+1][j] >= lines[i][j]: break
            y += 1

        score *= t

        result = max(result, score)

print(f'Result: {result}')
