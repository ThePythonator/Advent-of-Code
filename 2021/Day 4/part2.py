SIZE = 5

def check(board, nums):
    # Check columns
    for x in range(SIZE):
        c = 0
        for y in range(SIZE):
            if board[y][x] in nums:
                c += 1

        if c == SIZE:
            return True

    # Check rows
    for y in range(SIZE):
        c = 0
        for x in range(SIZE):
            if board[y][x] in nums:
                c += 1

        if c == SIZE:
            return True

    return False

def get_boards_complete(boards, nums):
    return [board for board in boards if check(board, nums)]

def get_score(board, nums):
    final = []
    for x in range(SIZE):
        for y in range(SIZE):
            if board[y][x] not in nums:
                final.append(board[y][x])
    return nums[-1] * sum(final)

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

boards = []
num_order = [int(item) for item in lines[0].split(',')]
nums = []

lines = lines[2:]

board = []
for line in lines:
    if line == '':
        boards.append(board)
        board = []

    else:
        board.append([int(item) for item in line.split(' ') if item != ''])
    
nums.append(num_order.pop(0))
while len(get_boards_complete(boards, nums)) < len(boards):
    last = get_boards_complete(boards, nums)
    nums.append(num_order.pop(0))

worst = [item for item in boards if item not in last][0]

print('Complete!')
#print(f'Score: {get_score(get_boards_complete(boards, nums)[0], nums)}')
print(f'Score: {get_score(worst, nums)}')
