import os
from functools import cache
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    lines = [line.strip() for line in f.readlines()]

def match(a, b): # b is letters
    return all([c == d or d == "?" for c, d in zip(a, b)])

def get_letters_nums(l, n):
    return "?".join([l.split(" ")[0]] * n), [int(z) for z in l.split(" ")[1].split(",")] * n

@cache
def generate_valid(n, nums, letters):
    if n < sum(nums) + len(nums) - 1:
        return 0
    elif n == sum(nums) + len(nums) - 1:
        if letters.count(".") > len(nums) - 1:
            return 0
        else:
            return 1 if match(".".join("#"*i for i in nums), letters) else 0
    elif len(nums) == 0:
        return 0 if "#" in letters else 1

    options = 0
    if letters[0] != "#":
        options = generate_valid(n - 1, nums, letters[1:])
    if match("#"*nums[0] + ".", letters[:nums[0]+1]):
        options += generate_valid(n - 1 - nums[0], nums[1:], letters[nums[0]+1:])
    
    return options


start = time()

result = 0
for i, line in enumerate(lines):
    letters, nums = get_letters_nums(line, 5)
    possibilities = generate_valid(len(letters), tuple(nums), letters)
    result += possibilities

print(f"Time: {time() - start}")
print(f"Result: {result}")
