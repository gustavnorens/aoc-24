import uf
from collections import defaultdict
lines = uf.read_lines("../input/12.in")
#lines = uf.read_lines("../tests/12.test")

#lines = [[c for c in line] for line in lines]



counter = 0
def sides(l):
    region = set(l)
    perimeter = []
    for x, y in l:
        for nx, ny in uf.cross(x, y):
            if (nx, ny) not in region:
                perimeter.append((nx,ny, (nx - x, ny - y)))
    sides = []
    visit = set()
    for (x,y,d) in perimeter:
        if (x,y,d) not in visit:
            side = flood2(x,y,d, perimeter)
            sides.append(side)
            for s in side:
                visit.add(s)
    print(sides)
    return len(sides)

def flood2(i,j,d, perimeter):
    stack = [(i, j, d)]
    sides = []
    while stack:
        current = stack.pop()
        if current in sides:
            continue
        sides.append(current)
        for nx, ny in uf.cross(current[0], current[1]):
            if (nx,ny,d) in perimeter:
              stack.append((nx,ny,d))
    return sides

def flood(i,j):
    stack = [(i,j)]
    region = []
    while stack:
        current = stack.pop()
        if current in region:
            continue
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
            region = flood(i,j)
            regions.append(region)
            for cord in region:
                visited.add(cord)
count = 0
for region in regions:
    s = sides(region)
    count += len(region) * s
    print(len(region), s)
print(count)
