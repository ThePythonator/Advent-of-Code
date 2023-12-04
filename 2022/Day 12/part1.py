class Dijkstra:
    def __init__(self, nodes, arcs, start, end):
        self._nodes = nodes
        self._arcs = arcs

        self._start = start
        self._end = end

        # input(arcs)

    def solve(self):
        current_node = self._start

        distances = {}
        previouses = {}

        q = []
        v = []

        q.append(self._start)

        self._arcs[self._start][self._start] = 0 # Bit hacky
        distances[self._start] = 0

        while len(q) > 0:
            current_dist = distances[q[0]] + 1
            for node in q:
                if distances[node] < current_dist:
                    current_node = node
                    current_dist = distances[node]

            for connected_node in self._arcs[current_node].keys():
                
                if connected_node not in v:
                    if connected_node not in distances.keys() or distances[connected_node] > distances[current_node] + self._arcs[current_node][connected_node]:
                        distances[connected_node] = distances[current_node] + self._arcs[current_node][connected_node]
                        previouses[connected_node] = current_node

                    if connected_node not in q:
                        q.append(connected_node)

            q.remove(current_node)
            v.append(current_node)

            # print(current_node, distances, q)
            # input()

        # print(self._end, len(previouses.keys()), len(arcs.keys()), len(distances.keys()))
        # input()

        v = self._end
        path = [v]
        while v != self._start:
            v = previouses[v]
            path = [v] + path

        return distances[self._end], path


with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

# lines = """Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi""".split('\n')

h = len(lines)
w = len(lines[0])

for y in range(h):
    for x in range(w):
        i = y * w + x
        
        c = lines[y][x]

        if c == 'S':
            start = i
            lines[y] = lines[y].replace('S', 'a')

        elif c == 'E':
            end = i
            lines[y] = lines[y].replace('E', 'z')

nodes = []
arcs = {}
for y in range(h):
    for x in range(w):
        i = y * w + x

        nodes.append(i)
        
        c = lines[y][x]

        arcs[i] = {}

        if x > 0 and ord(lines[y][x-1]) - ord(c) <= 1:
            arcs[i][i - 1] = 1

        if x < w - 1 and ord(lines[y][x+1]) - ord(c) <= 1:
            arcs[i][i + 1] = 1

        if y > 0 and ord(lines[y-1][x]) - ord(c) <= 1:
            arcs[i][i - w] = 1

        if y < h - 1 and ord(lines[y+1][x]) - ord(c) <= 1:
            arcs[i][i + w] = 1

result, path = Dijkstra(nodes, arcs, start, end).solve()

print(f'Result: {result}')
