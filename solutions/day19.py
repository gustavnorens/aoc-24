import uf
from collections import defaultdict

lines = uf.read("../input/19.in")  
#lines = uf.read("../tests/19.test")  

patterns, designs = lines.split("\n\n")

designs = designs.split("\n")
patterns = patterns.split(", ")

dp = defaultdict(int)
def find(design):
    if design == "":
        return 1
    if design in dp:
        return dp[design]
    for pattern in patterns:
        if len(pattern) <= len(design) and design.startswith(pattern):
            remaining = design[len(pattern):]
            dp[design] += find(remaining)
    return dp[design]

first = 0    
second = 0
for design in designs:
    result = find(design)
    if result > 0:
        first += 1
    second += find(design)

print(first, second)

