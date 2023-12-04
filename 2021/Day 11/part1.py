with open('input.txt') as f:
    octopi = [[int(o) for o in line.strip()] for line in f.readlines()]

##octopi = [[5,4,8,3,1,4,3,2,2,3],
##[2,7,4,5,8,5,4,7,1,1],
##[5,2,6,4,5,5,6,1,7,3],
##[6,1,4,1,3,3,6,1,4,6],
##[6,3,5,7,3,8,5,4,7,8],
##[4,1,6,7,5,2,4,6,4,5],
##[2,1,7,6,8,4,1,7,2,1],
##[6,8,8,2,8,8,1,1,3,4],
##[4,8,4,6,8,4,8,5,5,4],
##[5,2,8,3,7,5,1,5,2,6]
##]

##octopi = [[1,1,1,1,1],
##[1,9,9,9,1],
##[1,9,1,9,1],
##[1,9,9,9,1],
##[1,1,1,1,1]
##]

def step(grid):
    flashes = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid[y][x] += 1

    done = False
    while not done:
        done = True

        #for line in grid:print(line)
        #input()
        
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] > 9:
                    grid[y][x] = -1
                    flashes += 1
                    done = False

                    if y > 0 and grid[y-1][x] >= 0:
                        grid[y-1][x] += 1
                    if y > 0 and x > 0 and grid[y-1][x-1] >= 0:
                        grid[y-1][x-1] += 1
                    if x > 0 and grid[y][x-1] >= 0:
                        grid[y][x-1] += 1
                    if x > 0 and y < len(grid)-1 and grid[y+1][x-1] >= 0:
                        grid[y+1][x-1] += 1
                    if y < len(grid)-1 and grid[y+1][x] >= 0:
                        grid[y+1][x] += 1
                    if y < len(grid)-1 and x < len(grid[0])-1 and grid[y+1][x+1] >= 0:
                        grid[y+1][x+1] += 1
                    if x < len(grid[0])-1 and grid[y][x+1] >= 0:
                        grid[y][x+1] += 1
                    if x < len(grid[0])-1 and y > 0 and grid[y-1][x+1] >= 0:
                        grid[y-1][x+1] += 1

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] < 0:
                grid[y][x] = 0

    
    return flashes

total_flashes = 0
for i in range(100):
    total_flashes += step(octopi)

print(f'Result: {total_flashes}')
