def get_low_points(lines):
    lowest = []
    
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            low = True
            if x > 0:
                if lines[y][x] >= lines[y][x-1]:
                    low = False
            if y > 0:
                if lines[y][x] >= lines[y-1][x]:
                    low = False

            if x < len(lines[0]) - 1:
                if lines[y][x] >= lines[y][x+1]:
                    low = False
            if y < len(lines) - 1:
                if lines[y][x] >= lines[y+1][x]:
                    low = False

            if low:
                lowest.append(lines[y][x])

    return lowest

with open('input.txt') as f:
    lines = [[int(item) for item in line.strip()] for line in f.readlines()]

results = get_low_points(lines)

result = sum([item + 1 for item in results])

print(f'Result: {result}')
