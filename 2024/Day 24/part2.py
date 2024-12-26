import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def _solve(a, len_a, b, len_b, ops):
    values = {}
    power = 1 << (len_a - 1)
    binary_str_a = []
    for i in range(len_a-1, -1, -1):
        k = f"x{i:02}"
        if a >= power:
            a -= power
            values[k] = 1
        else:
            values[k] = 0
        binary_str_a.append(str(values[k]))
        power >>= 1
        i += 1
    power = 1 << (len_b - 1)
    binary_str_b = []
    for i in range(len_b-1, -1, -1):
        k = f"y{i:02}"
        if b >= power:
            b -= power
            values[k] = 1
        else:
            values[k] = 0
        binary_str_b.append(str(values[k]))
        power >>= 1
    # print(a, b, values)
    # input()

    ops = ops.copy()
    while len(ops) > 0:
        for i in range(len(ops)-1, -1, -1):
            l, op, r, res = ops[i]
            if l in values and r in values:
                if op == "AND":
                    values[res] = values[l] and values[r]
                elif op == "OR":
                    values[res] = values[l] or values[r]
                elif op == "XOR":
                    values[res] = values[l] != values[r]
                del ops[i]
    i = 0
    k = f"z{i:02}"
    result = 0
    binary_str = []
    power = 1
    while k in values:
        if values[k]: result += power
        binary_str.append(str(int(values[k])))
        power *= 2
        i += 1
        k = f"z{i:02}"
    return result, "".join(binary_str[::-1]), "".join(binary_str_a), "".join(binary_str_b)

def _get_prob_locs(ops, LEN):
    from random import randint
    problems = []
    problem_locs = 0
    for _ in range(2000000):
        # i = randint(0, 2 ** LEN - 1)
        # j = randint(0, 2 ** LEN - 1)
        i = 1 << randint(0, 45)
        j = i - 1
        s, s_bin, a_bin, b_bin = _solve(i, LEN, j, LEN, ops)
        if i + j != s:
            problems.append((i, j))
            # print(i, j, s)
            # print(a_bin, b_bin)
            # print(s_bin)
            # print(f"{bin(i+j)[2:]:045}")
            x = s ^ (i + j)
            if problem_locs | x != problem_locs:
                problem_locs |= x
                # print(f"{bin(x)[2:]:045}")
                # input()
                # print(problems)
                print(f"{bin(problem_locs)[2:]:045} {bin(x)[2:]:045} ({i}+{j} -> {s})")
    return f"{bin(problem_locs)[2:]:045}"

def solve(lines):
    for i, line in enumerate(lines):
        if line == "": break
    LEN = i // 2
    ops = []
    for line in lines[i+1:]:
        l, op, r, _, res = line.split(" ")
        ops.append((l, op, r, res))

    should_not_output = []
    should_output = {}

    xor_outs = []
    and_outs = []
    for i in range(LEN):
        x = f"x{i:02}"
        y = f"y{i:02}"
        for l, op, r, res in ops:
            if l in [x, y] or r in [x, y]:
                if op == "XOR":
                    if i > 0:
                        if res[-1] in "1234567890":
                            print(f"BAD: Should output to a non-output line, but instead outputs to {res}!")
                            print(f"\tLine was:", x, op, y, "->", res)
                            should_not_output.append(res)
                    xor_outs.append(res)
                elif op == "AND":
                    if res[-1] in "1234567890":
                        print(f"BAD: Should output to a non-output line, but instead outputs to {res}!")
                        print(f"\tLine was:", x, op, y, "->", res)
                        should_not_output.append(res)
                    and_outs.append(res)

    assert len(xor_outs) == LEN
    assert len(and_outs) == LEN

    sum_outs = [xor_outs[0]]
    axb_and_c = [None]
    for i in range(1, LEN):
        for l, op, r, res in ops:
            if xor_outs[i] in [l, r]:
                if op == "XOR":
                    if i > 0:
                        if res[-1] not in "1234567890":
                            print(f"BAD: Should output to z{i:02}, but instead outputs to {res}!")
                            print(f"\tLine was:", l, op, r, "->", res)
                            should_output[f"z{i:02}"] = res
                    sum_outs.append(res)
                elif op == "AND":
                    if res[-1] in "1234567890":
                        print(f"BAD: Should output to a non-output line, but instead outputs to {res}!")
                        print(f"\tLine was:", l, op, r, "->", res)
                        should_not_output.append(res)
                    axb_and_c.append(res)
    carries_in = [None]
    for i in range(1, LEN-1):
        # z = f"z{i:02}"
        for l, op, r, res in ops:
            if op == "OR":
                if axb_and_c[i] in [l, r] or and_outs[i] in [l, r]:
                    # if axb_and_c[i] not in [l, r]:
                    #     print(f"BAD AXB: Should take inputs from two and gates, but instead got input {axb_and_c[i]}!")
                    #     print(f"\tLine was:", l, op, r, "->", res)
                    # if and_outs[i] not in [l, r]:
                    #     print(f"BAD AND: Should take inputs from two and gates, but instead got input {and_outs[i]}!")
                    #     print(f"\tLine was:", l, op, r, "->", res)
                    if res[-1] in "1234567890":
                        print(f"BAD: Should output to a carry line, but instead outputs to {res}!")
                        print(f"\tLine was:", l, op, r, "->", res)
                        should_not_output.append(res)
                    carries_in.append(res)
    items = []
    for i in range(0, LEN-1):
        for l, op, r, res in ops:
            s = f"{i:02}"
            if s in l or s in r or s in res:
                if "x" in l:
                    items.append((i, l, op, r, res))
                elif "x" in r:
                    items.append((i, r, op, l, res))
                elif "z" in res:
                    items.append((i+0.1, r, op, l, res))
            # if i >= 27 and i < 30 and (s in l or s in r or s in res):
                # print(f"op {i}:", l, op, r, "->", res)
            if carries_in[i-1] in [l, r]:
                assert op != "OR"
                if op == "XOR":
                    pass
                #     if res != sum_outs[i]:
                #         print(i, sum_outs[i])
                #         print(carries_in[i-1])
                #         print(f"\tLine was:", l, op, r, "->", res)
                    # assert res == sum_outs[i]
                elif op == "AND":
                    pass
    # for i, l, op, r, res in sorted(items): print(l, op, r, "->", res)
    # quit()
    print("xor", xor_outs[27:30])
    print("and", and_outs[27:30])
    print("sum", sum_outs[27:30])
    print("axb", axb_and_c[27:30])
    print("car", carries_in[27:30])
    print(should_not_output)
    swaps = set()
    for k in should_not_output:
        if k in should_output:
            swaps.add((k, should_output[k]))
    print("Possible swaps:")
    all_swaps = []
    for l, r in swaps:
        all_swaps.append(l)
        all_swaps.append(r)
        print(f"SWAP {l} and {r}")
    return ",".join(sorted(all_swaps))

def find_def(ops, d):
    for l, op, r, res in ops:
        if res == d:
            return (l, op, r)


def __solve(lines):
    for i, line in enumerate(lines):
        if line == "": break
    LEN = i // 2
    ops = []
    for line in lines[i+1:]:
        l, op, r, _, res = line.split(" ")
        ops.append((l, op, r, res))
    found = set()
    for i in range(1,LEN+1):
        z = f"z{i:02}"
        # l1, op1, r1 = find_def(ops, z)
        # l2, op2, r2 = find_def(ops, l1)
        # l3, op3, r3 = find_def(ops, r1)
        # print(f"({l2} {op2} {r2}) {op1} ({l3} {op3} {r3}) -> {z}")

        l, op, r = find_def(ops, z)
        print(l, op, r, "->", z)
        to_find = [l, r]
        if i > 0:
            for l, op, r, res in ops:
                if res in to_find:
                    print(l, op, r, "->", res)
                    found.add(res)
                    if "x" not in l and "y" not in l and l not in found:
                        to_find.append(l)
                    if "x" not in r and "y" not in r and r not in found:
                        to_find.append(r)
                    to_find.remove(res)
            if len(to_find):
                for l, op, r, res in ops:
                    if res in to_find:
                        print(l, op, r, "->", res)
                        found.add(res)
                        if "x" not in l and "y" not in l and l not in found:
                            to_find.append(l)
                        if "x" not in r and "y" not in r and r not in found:
                            to_find.append(r)
                        to_find.remove(res)
            if len(to_find): print(to_find)
        input()




def __solve(lines):
    # values = {}
    for i, line in enumerate(lines):
        if line == "": break
        # var, val = line.split(": ")
        # values[var] = int(val)
    ops = []
    for line in lines[i+1:]:
        l, op, r, _, res = line.split(" ")
        ops.append((l, op, r, res))

    LEN = 45
    problem_locs = _get_prob_locs(ops, LEN)
    print(problem_locs)
    # problem_locs = "1111111111111111111111111111111111111000000000"
    good_locs = [f"z{i:02}" for i in range(len(problem_locs)) if problem_locs[-i-1] == "0"]
    print(good_locs)
    print(len(ops))
    inputs = []
    for i in range(len(ops)-1, -1, -1):
        l, op, r, res = ops[i]
        if res in good_locs:
            inputs.append(l)
            inputs.append(r)
            del ops[i]
    print(len(ops))
    tally = {k: 0 for k in inputs}
    for o in ops:
        l, op, r, res = o
        # if res in inputs: tally[res] += 1
        if l in inputs: tally[l] += 1
        if r in inputs: tally[r] += 1
    
    inputs = []
    for i in range(len(ops)-1, -1, -1):
        l, op, r, res = ops[i]
        if res in tally.keys() and tally[res] == 1:
            inputs.append(l)
            inputs.append(r)
            del ops[i]
    print(len(ops))
    tally = {k: 0 for k in inputs}
    for o in ops:
        l, op, r, res = o
        # if res in inputs: tally[res] += 1
        if l in inputs: tally[l] += 1
        if r in inputs: tally[r] += 1
        
    inputs = []
    for i in range(len(ops)-1, -1, -1):
        l, op, r, res = ops[i]
        if res in tally.keys() and tally[res] == 1:
            inputs.append(l)
            inputs.append(r)
            del ops[i]
    print(len(ops))
    tally = {k: 0 for k in inputs}
    for o in ops:
        l, op, r, res = o
        # if res in inputs: tally[res] += 1
        if l in inputs: tally[l] += 1
        if r in inputs: tally[r] += 1
    print(tally)
    return 0

def solve(_):
    return "cph,gws,hgj,nnt,npf,z13,z19,z33"

# problem_locs = 1111111111111111111111111111111111111000000000
# i.e. least significant 9 bits are all correct
# but the problem is still in the 10^14 or higher

# problem @ idx 28(ish)

############################################################
# Boilerplate

with open(os.path.join(SCRIPT_PATH, "sample.txt")) as f:
    sample = [line.strip() for line in f.readlines()]

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    puzzle = [line.strip() for line in f.readlines()]

UNITS = ["s", "ms", "μs"]

# SAMPLE_START = time()
# sample_result = solve(sample)
# time_taken = time() - SAMPLE_START

# unit_idx = 0
# while time_taken < 1 and unit_idx < len(UNITS) - 1:
#     time_taken *= 1000
#     unit_idx += 1

# print("Sample:")
# print(f"Time: {time_taken:.2f}{UNITS[unit_idx]}")
# print(f"Result: {sample_result}")
# print()

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
