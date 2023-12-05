import os
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    lines = [line.strip() for line in f.readlines()]

def fewest(line):
    m_r = m_g = m_b = 0
    subsets = line.split(": ")[1].split("; ")
    for subset in subsets:
        pairs = {l.split(" ")[1]: int(l.split(" ")[0]) for l in subset.split(", ")}
        r = pairs.get("red", 0)
        g = pairs.get("green", 0)
        b = pairs.get("blue", 0)
        
        m_r = max(m_r, r)
        m_g = max(m_g, g)
        m_b = max(m_b, b)
    
    return m_r, m_g, m_b

result = 0
for i, line in enumerate(lines, 1):
    r, g, b = fewest(line)
    result += r * g * b

print(f'Result: {result}')
