import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

class FlipFlop:
    def __init__(self, name, outputs):
        self.name = name
        self.outputs = outputs
        self.state = 0 # Initially low

    def add_input(self, _):
        return

    def input(self, source, pulse):
        if pulse == 0: # Low pulse
            self.state = 1 - self.state
            return [(self.name, output, self.state) for output in self.outputs]
        else:
            return []

class Conjunction:
    def __init__(self, name, outputs):
        self.name = name
        self.outputs = outputs
        self.memory = {}

    def add_input(self, i):
        self.memory[i] = 0

    def input(self, source, pulse):
        self.memory[source] = pulse
        result = 0 if all(v == 1 for v in self.memory.values()) else 1
        return [(self.name, output, result) for output in self.outputs]
    
class Broadcaster:
    def __init__(self, name, outputs):
        self.name = name
        self.outputs = outputs
    
    def input(self, source, pulse):
        return [(self.name, output, pulse) for output in self.outputs]
    
def simulate(modules):
    # Simulate
    q = [("button", "broadcaster", 0)]
    pulses = [0, 0]
    while len(q) > 0:
        source, module, pulse = q.pop(0)
        pulses[pulse] += 1
        if module in modules:
            q += modules[module].input(source, pulse)
    return pulses

def solve(lines):
    modules = {}
    for line in lines:
        source, dest = line.split(" -> ")
        t = source[0]
        name = source[1:]
        outputs = dest.split(", ")
        if t == "%":
            modules[name] = FlipFlop(name, outputs)
        elif t == "&":
            modules[name] = Conjunction(name, outputs)
        elif t == "b":
            modules[source] = Broadcaster(source, outputs)

    for line in lines:
        source, dest = line.split(" -> ")
        name = source[1:]
        if source[0] == "b":
            name = source
        outputs = dest.split(", ")
        for output in outputs:
            if output in modules:
                modules[output].add_input(name)

    lows = 0
    highs = 0
    for i in range(1000):
        l, h = simulate(modules)
        lows += l
        highs += h
    
    return lows * highs


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
