import math, functools

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

_lines = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II""".split('\n')

class Floyd:
    def __init__(self, vertices, edges):
        self._vertices = vertices
        self._edges = edges
        self._shortest_distances = {}

    def solve(self):
        for i in self._vertices:
            self._shortest_distances[i] = {}

            for j in self._vertices:
                self._shortest_distances[i][j] = math.inf

        for edge in self._edges.keys():
            self._shortest_distances[edge[0]][edge[1]] = self._edges[edge]

        for vertex in self._vertices:
            self._shortest_distances[vertex][vertex] = 0

        for k in self._vertices:
            for i in self._vertices:
                for j in self._vertices:
                    self._shortest_distances[i][j] = min(self._shortest_distances[i][j], self._shortest_distances[i][k] + self._shortest_distances[k][j])

        return self._shortest_distances

v = []
e = {}
flows = {}
for line in lines:
    room = line.split(' ')[1]
    flow = int(line.split('=')[1].split(';')[0])

    adjacent = ''.join(line.split(' ')[9:]).split(',')

    v.append(room)

    for a in adjacent:
        e[(room, a)] = 1

    flows[room] = flow

filtered = [z for z in v if flows[z] > 0]

t_dist = Floyd(v, e).solve()

dist = {}

for k in t_dist.keys():
    if flows[k] > 0 or k == 'AA':
        dist[k] = {}

        for j in t_dist.keys():
            if flows[j] > 0 and t_dist[k][j] > 0:
                dist[k][j] = t_dist[k][j]

@functools.cache
def value(node, t, visited, e):
    r = 0

    new_visited = set(visited)
    new_visited.add(node)
    new_visited = frozenset(new_visited)

    if e:
        r = value('AA', 26, new_visited, False)

    for p in dist[node].keys():
        if p not in visited and t > dist[node][p]:
            new_t = t - dist[node][p] - 1
            val = flows[p] * new_t
            r = max(r, val + value(p, new_t, new_visited, e))

    return r
    
def solve():
    return value('AA', 26, frozenset(), True)

#2581 too low
result = solve()

print(f'Result: {result}')