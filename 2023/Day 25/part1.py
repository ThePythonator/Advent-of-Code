import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def solve(lines):
    result = 0
    graph = {}
    for line in lines:
        l, rs = line.split(": ")
        rs = rs.split(" ")
        if l not in graph:
            graph[l] = {}
        for r in rs:
            # arc tuples are (residual capacity, flow)
            graph[l][r] = (1,0)
            if r not in graph:
                graph[r] = {}
            graph[r][l] = (1,0)

    # for k, v in graph.items():
    #     for _v, i in v.items():
    #         print(f"{k} -> {_v}: {i}")
    starts = list(graph.keys())
    source = starts.pop(0)
    sink = starts.pop(0)
    total_flow = 0
    while True:
        # BFS to find an augmenting path
        q = [([source], 1)] # Start at the source - there can never be more than an augmenting flow of 1
        visited = set()
        augmenting_path = None
        augmenting_amount = None
        while len(q) > 0:
            path, spare = q.pop(0)
            node = path[-1]
            if node == sink:
                augmenting_path = path
                augmenting_amount = spare
                break
            if node in visited:
                continue
            visited.add(node)
            for e, (resi, flow) in graph[node].items():
                if resi > 0:
                    q.append((path + [e], min(spare, resi)))
        if augmenting_path is None:
            break
        # Augment the path
        for i in range(len(augmenting_path) - 1):
            start = augmenting_path[i]
            end = augmenting_path[i+1]
            resi, flow = graph[start][end]
            graph[start][end] = (resi - augmenting_amount, flow + augmenting_amount)
        total_flow += augmenting_amount
        if total_flow > 3:
            # Reset
            sink = starts.pop(0)
            total_flow = 0
            for k in graph.keys():
                for e in graph[k].keys():
                    graph[k][e] = (1,0)

    assert total_flow == 3
    return len(visited) * (len(graph) - len(visited))


############################################################
# Boilerplate

with open(os.path.join(SCRIPT_PATH, "sample.txt")) as f:
    sample = [line.strip() for line in f.readlines()]

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    puzzle = [line.strip() for line in f.readlines()]

SAMPLE_START = time()
sample_result = solve(sample)
print("Sample:")
print(f"Time: {time() - SAMPLE_START}")
print(f"Result: {sample_result}")
print()

PUZZLE_START = time()
puzzle_result = solve(puzzle)
print("Puzzle:")
print(f"Time: {time() - PUZZLE_START}")
print(f"Result: {puzzle_result}")
