import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

from functools import cache

############################################################
# Main solution code here

def solve(lines):
    shapes = []
    areas = []
    shape = []
    area = 0
    trees = []
    for i, line in enumerate(lines):
        if line == "" and len(shape):
            shapes.append(shape)
            areas.append(area)
            shape = []
            area = 0
            continue
        elif "x" in line:
            region, *nums = line.split(" ")
            region = [int(v) for v in region.replace(":", "").split("x")]
            region.sort(reverse=True)
            nums = [int(v) for v in nums]
            trees.append((region, nums))
            # print(region, nums)
        elif ":" in line:
            continue
        elif "#" in line or "." in line:
            shape.append(line)
            area += line.count("#")
            # shape.append(int(line.replace("#","1").replace(".","0"), base=2))
    
    # def shape_to_int(shape):
    #     vals = []
    #     for line in shape:
    #         vals.append(int(line.replace("#","1").replace(".","0"), base=2))
    #     return tuple(vals)

    def shape_to_int(shape):
        return tuple(tuple(c == "#" for c in line) for line in shape)

    shape_options = []
    for shape in shapes:
        options = set()
        # Original
        options.add(shape_to_int(shape))
        # Flip left to right
        options.add(shape_to_int(line[::-1] for line in shape))
        # Flip top to bottom
        options.add(shape_to_int(shape[::-1]))
        # Flip in both directions
        options.add(shape_to_int(line[::-1] for line in shape[::-1]))
        # Rotate 90 CW
        options.add(shape_to_int("".join(shape[y][x] for y in range(len(shape)-1,-1,-1)) for x in range(len(shape[0]))))
        # Rotate 90 ACW
        options.add(shape_to_int("".join(shape[y][x] for y in range(len(shape))) for x in range(len(shape[0])-1,-1,-1)))
        # Rotate 90 CW (flipped in vertical)
        options.add(shape_to_int("".join(shape[y][x] for y in range(len(shape))) for x in range(len(shape[0]))))
        # Rotate 90 ACW (flipped in vertical)
        options.add(shape_to_int("".join(shape[y][x] for y in range(len(shape)-1,-1,-1)) for x in range(len(shape[0])-1,-1,-1)))
        
        shape_options.append(options)

    # print(shapes)
    # print(shape_options)

    def make_repr(region, r):
        grid = [["." for _ in range(region[0])] for _ in range(region[1])]
        for w, (x, y, idx, shape) in enumerate(r):
            for dy in range(len(shape)):
                for dx in range(len(shape[0])):
                    if shape[dy][dx]:
                        grid[y+dy][x+dx] = "ABCDEFGHIJKLMNO"[w]
        return ["".join(line) for line in grid]

    def print_grid(grid):
        for line in grid: print("".join(["#" if c else "." for c in line]) )

    def fits(region, grid, shape, x, y):
        for dy in range(len(shape)):
            for dx in range(len(shape[0])):
                if x+dx >= region[0] or y+dy >= region[1] or (grid[y+dy][x+dx] and shape[dy][dx]):
                    return False
        return True

    def fit(region, grid, remaining_nums, fast=False, get_grid=False):
        # print("fit", region, remaining_nums)
        if sum(remaining_nums) == 0:
            # return []
            return grid if get_grid else True

        valid_shapes = [idx for idx, num in enumerate(remaining_nums) if num > 0]

        x = y = 0
        found_valid = False
        while True:
            # print(region, remaining_nums, x, y)
            # for line in grid: print("".join("#" if c else "." for c in line))
            # input()

            if found_valid and fast:
                return None if get_grid else False

            # Try and fit a shape
            for idx in valid_shapes:
                for shape in shape_options[idx]:
                    if fits(region, grid, shape, x, y):
                        found_valid = True
                        # Fit shape in
                        new_grid = [line.copy() for line in grid]
                        for dy in range(len(shape)):
                            for dx in range(len(shape[0])):
                                new_grid[y+dy][x+dx] = new_grid[y+dy][x+dx] or shape[dy][dx]
                        new_remaining_nums = [num - 1 if i == idx else num for i, num in enumerate(remaining_nums)]
                        r = fit(region, new_grid, new_remaining_nums, fast, get_grid)
                        if r: return r
                        # r = fit(region, new_grid, new_remaining_nums)
                        # if r is not None:
                        #     return [(x, y, idx, shape)] + r

            x += 1
            if x >= region[0]:
                x = 0
                y += 1
                if y >= region[1]:
                    return None if get_grid else False
                    # return None

    fast_4x3 = []
    fast_4x4 = []
    fast_5x4 = []
    for i in range(len(shapes)):
        for j in range(i, len(shapes)):
            _nums = [0] * len(shapes)
            _nums[i] += 1
            _nums[j] += 1

            _4x3 = [[False for _ in range(4)] for _ in range(3)]
            _4x4 = [[False for _ in range(4)] for _ in range(4)]
            _5x4 = [[False for _ in range(5)] for _ in range(4)]

            grid = fit([4,3], _4x3, _nums, get_grid=True)
            if grid:
                area = sum(sum(1 for c in row if c) for row in grid)
                fast_4x3.append((area, i, j, grid))
                continue

            grid = fit([4,4], _4x4, _nums, get_grid=True)
            if grid:
                area = sum(sum(1 for c in row if c) for row in grid)
                fast_4x4.append((area, i, j, grid))
                continue
                
            grid = fit([5,4], _5x4, _nums, get_grid=True)
            if grid:
                area = sum(sum(1 for c in row if c) for row in grid)
                fast_5x4.append((area, i, j, grid))
                continue
            # print(i,j)

    fast_4x3.sort(reverse=True)
    fast_4x4.sort(reverse=True)
    fast_5x4.sort(reverse=True)

    # print(fast_4x3)
    # print(fast_4x4)
    # print(fast_5x4)
    # print("4x3")
    # for area, i, j, grid in fast_4x3:
    #     print(area, i, j)
    #     # print_grid(grid)
    # # input()

    # print("4x4")
    # for area, i, j, grid in fast_4x4:
    #     print(area, i, j)
    #     # print_grid(grid)
    # # input()
        
    # print("5x4")
    # for area, i, j, grid in fast_5x4:
    #     print(area, i, j)
    #     # print_grid(grid)
    # # input()

    def fast_fit(region, grid, remaining_nums):
        if sum(remaining_nums) == 0:
            return True
        # Use some harcoded shortcuts
        x = y = 0
        while y < region[1]:
            for area, i, j, shape in fast_4x3 + fast_4x4 + fast_5x4:
                # print(i, j, shape)
                # print_grid(shape)
                if (i == j and remaining_nums[i] >= 2) or (i != j and remaining_nums[i] >= 1 and remaining_nums[j] >= 1):
                    if fits(region, grid, shape, x, y):
                        new_grid = [line.copy() for line in grid]
                        for dy in range(len(shape)):
                            for dx in range(len(shape[0])):
                                new_grid[y+dy][x+dx] = new_grid[y+dy][x+dx] or shape[dy][dx]
                        new_remaining_nums = remaining_nums.copy()
                        new_remaining_nums[i] -= 1
                        new_remaining_nums[j] -= 1
                        r = fast_fit(region, new_grid, new_remaining_nums)
                        if r: return r
            
            x += 1
            if x >= region[0]:
                x = 0
                y += 1

        # print(f"Fast fit ended for {region} with remaining {remaining_nums}. Grid is:")
        # print_grid(grid)
        # input()
        return fit(region, grid, remaining_nums, fast=True)

    result = 0
    for z, (region, nums) in enumerate(trees):
        total_area = 0
        for i, num in enumerate(nums):
            if num == 0: continue
            # print(i, num, shape_options[i])
            total_area += num * areas[i]
        if (region[0] // 3) * (region[1] // 3) >= sum(nums):
            # Easy
            # print(f"SUCCESS ({z+1}/{len(trees)}) - EASY")
            result += 1
            continue
        elif region[0] * region[1] < total_area:
            # print(f"FAIL ({z+1}/{len(trees)}) - EASY")
            continue
        # print(f"Skip ({z+1}/{len(trees)})...")
        # continue
        # Try to fit everything in
        grid = [[False for _ in range(region[0])] for _ in range(region[1])]
        # if fit(region, grid, nums):
        if fast_fit(region, grid, nums):
        # r = fit(region, grid, nums)
        # if r is not None:
            # for line in make_repr(region, r): print(line)
            # print(f"SUCCESS ({z+1}/{len(trees)})")
            result += 1
        # else:
            # print(f"FAIL ({z+1}/{len(trees)})")
    return result

# Lower bound for input: 469

############################################################
# Boilerplate

with open(os.path.join(SCRIPT_PATH, "sample.txt")) as f:
    sample = [line.strip() for line in f.readlines()]

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    puzzle = [line.strip() for line in f.readlines()]

UNITS = ["s", "ms", "μs"]

SAMPLE_START = time()
sample_result = solve(sample)
time_taken = time() - SAMPLE_START

unit_idx = 0
while time_taken < 1 and unit_idx < len(UNITS) - 1:
    time_taken *= 1000
    unit_idx += 1

print("Sample:")
print(f"Time: {time_taken:.2f}{UNITS[unit_idx]}")
print(f"Result: {sample_result}")
print()

PUZZLE_START = time()
puzzle_result = solve(puzzle)
time_taken = time() - PUZZLE_START

unit_idx = 0
while time_taken < 1 and unit_idx < len(UNITS) - 1:
    time_taken *= 1000
    unit_idx += 1

print("Puzzle:")
print(f"Time: {time_taken:.2f}{UNITS[unit_idx]}")
print(f"Result: {puzzle_result}")
