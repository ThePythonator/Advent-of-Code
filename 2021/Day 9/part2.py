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
                lowest.append([x, y])

    return lowest

def count_higher_points(lines, point):
    count = 1

    BLANK = 0
    
    if point[0] > 0 and lines[point[1]][point[0]-1] < 9 and lines[point[1]][point[0]] < lines[point[1]][point[0]-1]:
        count += count_higher_points(lines, [point[0]-1, point[1]])

    if point[1] > 0 and lines[point[1]-1][point[0]] < 9 and lines[point[1]][point[0]] < lines[point[1]-1][point[0]]:
        count += count_higher_points(lines, [point[0], point[1]-1])

    if point[0] < len(lines[0]) - 1 and lines[point[1]][point[0]+1] < 9 and lines[point[1]][point[0]] < lines[point[1]][point[0]+1]:
        count += count_higher_points(lines, [point[0]+1, point[1]])

    if point[1] < len(lines) - 1 and lines[point[1]+1][point[0]] < 9 and lines[point[1]][point[0]] < lines[point[1]+1][point[0]]:
        count += count_higher_points(lines, [point[0], point[1]+1])

    lines[point[1]][point[0]] = BLANK
    
    return count

def get_basin_size(lines, low_point):
    size = 0
    temp = lines.copy()

    size += count_higher_points(temp, low_point)

    return size

def product(a):
    total = 1
    for item in a:
        total *= item
    return total

with open('input.txt') as f:
    lines = [[int(item) for item in line.strip()] for line in f.readlines()]

sizes = [get_basin_size(lines, low_point) for low_point in get_low_points(lines)]
sizes.sort(reverse=True)

result = product(sizes[:3])
print(f'Result: {result}')
