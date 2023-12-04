with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

grid = [[0]*1000 for i in range(1000)]

result = 0
for line in lines:
    s = line.split(' ')

    start = [int(i) for i in s[-3].split(',')]
    end = [int(i) for i in s[-1].split(',')]

    for x in range(start[0], end[0]+1):
        for y in range(start[1], end[1]+1):
            if s[0] == "toggle":
                grid[y][x] += 2
            
            elif s[1] == "on":
                grid[y][x] += 1

            elif s[1] == "off":
                grid[y][x] = max(grid[y][x] - 1, 0)

result = sum([sum(row) for row in grid])

print(f'Result: {result}')



# def sum2D(iterable):
#     total = 0
#     for l in iterable:
#         total += sum(l)
#     return total
    
# for line in lines:
#     splitted = line.split(' ')
#     stop = splitted.pop(-1).split(',')
#     stop = [int(stop[0]),int(stop[1])]
#     splitted.pop(-1) # ignore 'through'
#     start = splitted.pop(-1).split(',')
#     start = [int(start[0]),int(start[1])]
#     op = ''.join(splitted)
    
#     for y in range(start[1],stop[1]+1):
#         for x in range(start[0],stop[0]+1):
#             if op == 'turnon':
#                 lights[y][x] += 1
#             elif op == 'turnoff':
#                 lights[y][x] = max(0, lights[y][x]-1)
#             elif op == 'toggle':
#                 lights[y][x] += 2

# print(sum2D(lights))
