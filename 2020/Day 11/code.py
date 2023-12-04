##def get_adjacents(grid,x,y):
##    adjacents = []
##
##    if y > 0:
##        adjacents.append(grid[y-1][x])
##
##    if y < len(grid)-1:
##        adjacents.append(grid[y+1][x])
##
##    if x > 0:
##        adjacents.append(grid[y][x-1])
##        
##        if y > 0:
##            adjacents.append(grid[y-1][x-1])
##
##        if y < len(grid)-1:
##            adjacents.append(grid[y+1][x-1])
##
##    if x < len(grid[0])-1:
##        adjacents.append(grid[y][x+1])
##        
##        if y > 0:
##            adjacents.append(grid[y-1][x+1])
##
##        if y < len(grid)-1:
##            adjacents.append(grid[y+1][x+1])
##
##    return adjacents

def get_adjacents(grid,x,y):
    adjacents = []

    for shift in [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]:
        viewx,viewy = x,y
        cont = True
        viewx += shift[0]
        viewy += shift[1]
        while cont and viewx >= 0 and viewx < len(grid[0]) and viewy >= 0 and viewy < len(grid):
            if grid[viewy][viewx] != '.':
                cont = False
                adjacents.append(grid[viewy][viewx])
            viewx += shift[0]
            viewy += shift[1]
    return adjacents  

with open('in.txt') as f:
    grid = [line.strip() for line in f.readlines()]

running = True
newGrid = grid.copy()
while running:
    running = False
    
    grid = newGrid
    newGrid = grid.copy()

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            adjacents = get_adjacents(grid,x,y)
            if grid[y][x] == 'L':
                if '#' not in adjacents:
                    newGrid[y] = newGrid[y][:x]+'#'+newGrid[y][x+1:]
                    running = True

            elif grid[y][x] == '#':
                count = adjacents.count('#')
                if count >= 5:
                    newGrid[y] = newGrid[y][:x]+'L'+newGrid[y][x+1:]
                    running = True
total = 0
for row in grid:
    total += row.count('#')

print(total)
