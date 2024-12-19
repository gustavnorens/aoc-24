import uf
from collections import deque
import copy

lines = uf.read_lines("../input/18.in")  
#lines = uf.read_lines("../tests/18.test")  

coords = []
for line in lines:
    coords.append(list(map(int, line.split(","))))

N = 71
M = 71

p1 = [["." for _ in range(M)] for _ in range(N)]
p2 = copy.deepcopy(p1)


def solve(grid):
    queue = deque([(0,0, 0)])
    visited = set()
    while queue:
        x,y, cost = queue.popleft()
        if (x,y) in visited:
            continue
        visited.add((x,y))
        if (x,y) == (N-1,M-1):
            return cost
        for nx,ny in uf.cross(x,y):
            if nx >= 0 and nx < N and ny >= 0 and ny < M and grid[nx][ny] != "#":
                queue.append((nx,ny, cost + 1))
    print(str(coords[i][0]) + "," + str(coords[i][1]))
    return -1

for i in range(1024):
    y,x = coords[i]
    p1[x][y] = "#"
print(solve(p1))
for i in range(len(coords)):
    y,x = coords[i]
    p2[x][y] = "#"
    if solve(p2) == -1:
        break