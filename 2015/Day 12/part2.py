import json

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

def traverse(j):
    if type(j) == dict and "red" in j.values():
        return 0

    if type(j) == str:
        return 0

    if type(j) == int:
        return j
    
    if type(j) == list:
        return sum([traverse(i) for i in j])

    if type(j) == dict:
        return sum([traverse(i) for i in j.values()])

    print(j)
    input("oops")


l = json.loads(lines[0])

result = traverse(l)

print(f'Result: {result}')