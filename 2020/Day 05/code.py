with open('in.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    
seats = list(range(128*8))
maxNum = 0

for line in lines:
    binaryRow = ''
    for c in line[:7]:
        binaryRow += '0' if c == 'F' else '1'

    binaryColumn = ''
    for c in line[7:]:
        binaryColumn += '0' if c == 'L' else '1'

    row = int(binaryRow, 2)
    column = int(binaryColumn, 2)
    
    num = 8*row + column
    
    seats.remove(num)
##    if num > maxNum:
##        maxNum = num


print(seats)
