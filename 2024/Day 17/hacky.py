# valid = {'111100010101111010111111', '101100010101111001101101', '111100010101111001101101', '100100010101111010111111', '111100100101111010111111', '111100100101111001101101', '000100010101111001101101', '000100010101111010111111', '100100010101111001101101', '101100010101111010111111'}
# valid = {'111010101000100010101111010111111', '111000101000100010101111010111111', '100100100111100010101111001101101', '111010101000100010101111001101101', '111010101111100100101111010111111', '111000101101100010101111001101101', '111000101111100010101111010111111', '111000101000100010101111001101101', '111010101111100010101111001101101', '111110101111100100101111010111111', '101010100111100010101111010111111', '111110101111100100101111001101101', '111110101111100010101111010111111', '100100100111100010101111010111111', '111000101111100100101111001101101', '111000101111100100101111010111111', '101100100111100010101111010111111', '111010101111100100101111001101101', '111000101111100010101111001101101', '111000101101100010101111010111111', '111010101111100010101111010111111', '101100100111100010101111001101101', '111110101000100010101111001101101', '101010100111100010101111001101101', '111110101000100010101111010111111', '111110101111100010101111001101101'}
# valid = {'010101101010100111100010101111010111111', '010101101010100111100010101111001101101'}
valid = {'001101101', '100100000', '010100000', '010111111'}
valid = {'001010111111', '111010111111', '111001101101'}
valid = {'101111001101101', '101111010111111'}
valid = {'010101111010111111', '010101111001101101', '100101111001101101', '100101111010111111'}
valid = {'100010101111010111111', '100100101111010111111', '100010101111001101101', '100100101111001101101'}
valid = {'000100010101111010111111', '000100010101111001101101', '111100010101111010111111', '111100100101111010111111', '101100010101111010111111', '111100100101111001101101', '111100010101111001101101', '101100010101111001101101'}
valid = {'101111100010101111001101101', '100111100010101111001101101', '101111100010101111010111111', '101101100010101111001101101', '101000100010101111001101101', '100111100010101111010111111', '101111100100101111010111111', '101000100010101111010111111', '101111100100101111001101101', '101101100010101111010111111'}
valid = {'010100111100010101111001101101', '010100111100010101111010111111'}
valid = {'101010100111100010101111001101101', '101010100111100010101111010111111'}
valid = {'101101010100111100010101111001101101', '101101010100111100010101111010111111'}

valid = [int(v, base=2) for v in valid]

def _solve(reg_a, target):
    reg_b = 0
    output_idx = 0
    output = []
    while True:
        reg_b = (reg_a % 8) ^ 3
        reg_b ^= (reg_a >> reg_b) ^ 5
        reg_a >>= 3
        if output_idx >= len(target) or target[output_idx] != reg_b % 8:
            return False
        output.append(reg_b % 8)
        output_idx += 1
        if reg_a == 0:
            return output_idx == len(target)
            # return output

def find_start(reg_a, target):
    reg_b = 0
    output_idx = 0
    while True:
        reg_b = (reg_a % 8) ^ 3
        reg_b ^= (reg_a >> reg_b) ^ 5
        reg_a >>= 3
        if target[output_idx] != reg_b % 8:
            return False
        output_idx += 1
        if reg_a == 0:
            return output_idx == len(target)
        if output_idx == len(target):
            return True

# This solved it by iteratively finding the binary suffix which makes the first few values in the program
# Then store all unique possible values and repeat for the next length of string

def solve():
    assert _solve(45483412, [1,5,0,5,2,0,1,3,5])
    target = [2,4,1,3,7,5,0,3,4,1,1,5,5,5,3,0]
    t = 0
    test_set = set()
    for i in range(0, 1000000):
        for v in valid:
            j = (i << 36) + v
            # if i % 1000000 == 0: print(f"Trying {i}...")
            # 140737488355328 + 3 * 500000000
            result = find_start(j, [2,4,1,3,7,5,0,3,4,1,1,5,5,5,3,0])
            if result:
                # return i
                if t == 0: print(j)
                t += 1
                test_set.add(bin(j)[-39:])
    print(test_set)
    return t

result = solve()
print(f"Result: {result}")

# 110101110010101101010100111100010101111010111111

# 236581108670143 (too high)
# 236581108670061

# Program structure:
2,4, # reg[1] = reg[0] % 8
1,3, # reg[1] ^= 3
7,5, # reg[0] = int(reg[0] // (1 << reg[1]))
0,3, # reg[2] = int(reg[0] // (1 << 3))
4,1, # reg[1] ^= reg[2]
1,5, # reg[1] ^= 5
5,5, # out (reg[1] % 8)
3,0, # if reg[0] != 0, jump to start
