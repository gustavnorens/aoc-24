import uf
import copy
import heapq
from collections import defaultdict

lines = uf.read_lines("../input/16.in")  
#lines = uf.read_lines("../tests/16.test")  

grid = [
        "#######",
        "#....E#",
        "#.##..#",
        "#.#..##",
        "#S....#",
        "#######"
        
        ]

grid = [[c for c in line] for line in lines]
N = len(grid)
M = len(grid[0])
g = {}

directions = [(-1,0),(0,1),(1,0),(0,-1)]
for i in range(N):
    for j in range(M):
            for d in range(4):
                g[(i,j,d)] = []
ex, ey = 0,0

for i in range(1,N-1):
    for j in range(1, M-1):
        if grid[i][j] == "E":
            ex, ey = i, j
        if grid[i][j] == "S":
            sx, sy = i, j
        if grid[i][j] != "#":
            for d in range(4):
                dx, dy = directions[d]
                nx, ny = i + dx, j + dy
                if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] != "#":
                    g[(i, j, d)].append((1, nx, ny, d))
                g[(i, j, d)].append((1000, i, j, (d + 1) % 4))
                g[(i, j, d)].append((1000, i, j, (d - 1) % 4))
                
def findPath(path, start):
     ret = [start]
     while True:
            if start not in path:
               return ret
            start = path[start]
            ret.append(start)

def dijkstra(start, graph):
    x,y,d = start
    pq = []
    path = {}
    heapq.heappush(pq, (0,start,start))
    visited = set()
    while pq:
        cost,src,dst = heapq.heappop(pq)
        if dst not in path:
            path[dst] = (src, cost)
        if dst in visited:
            continue
        visited.add(dst)
        for ncost,nx,ny,nd in graph[dst]:
            ndst = nx, ny, nd
            heapq.heappush(pq, (ncost + cost, dst, ndst))
    return path

def solve(shortest, graph, start):
    final = []
    stack = [(start, 0, [start])]
    memo = {}
    while stack:
        curr, score, path = stack.pop()
        x, y, _ = curr
        if curr in memo and memo[curr] < score:
            continue
        memo[curr] = score
        if (x,y) == (ex,ey) and score <= shortest:
            final.append(path)
        for ncost, nx, ny, nd in graph[curr]:
            new = (nx, ny, nd)
            new_score = ncost + score
            if new_score <= shortest:
                stack.append((new, new_score, path + [new]))
    return final
    
path = dijkstra((sx,sy,1), g)
num = path[ex,ey,0][1]

count = set()
paths = solve(num, g, (sx,sy,1))
for path in paths:
    for x,y,d in path:
        count.add((x,y))
print(num,len(count))