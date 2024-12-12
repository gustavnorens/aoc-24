import uf
from collections import defaultdict
lines = uf.read_lines("../input/12.in")
#lines = uf.read_lines("../tests/12.test")

def solve(l):
    region = set(l)
    perimeter = []
    for x, y in l:
        for nx, ny in uf.cross(x, y):
            if (nx, ny) not in region:
                perimeter.append((nx,ny, (nx - x, ny - y)))
    sides = []
    visited = set()
    for (x,y,d) in perimeter:
        if (x,y,d) not in visited:
            side = unifySides(x,y,d, perimeter, visited)
            sides.append(side)
    return len(perimeter), len(sides)

def unifySides(i,j,d, perimeter, visited):
    stack = [(i, j, d)]
    sides = []
    while stack:
        x, y, dire = stack.pop()
        if (x,y,dire) in visited:
            continue
        visited.add((x,y,dire))
        sides.append((x,y,dire))
        for nx, ny in uf.cross(x, y):
            if (nx,ny,d) in perimeter:
              stack.append((nx,ny,d))
    return sides

def flowerRegion(i,j, visited):
    stack = [(i,j)]
    region = []
    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        region.append(current)
        for nx, ny in uf.cross(*current):
            if nx >= 0 and nx < N and ny >= 0 and ny < M and lines[nx][ny] == lines[i][j]:
                stack.append((nx, ny))
    return region

N = len(lines)
M = len(lines[0])
visited = set()
regions = []

for i in range(N):
    for j in range(M):
        if (i,j) not in visited:
            region = flowerRegion(i,j, visited)
            regions.append(region)

first = 0
second = 0
for region in regions:
    perimeter, sideLength  = solve(region)
    first += len(region) * perimeter
    second += len(region * sideLength)
print(first, second)
