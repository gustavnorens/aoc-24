import uf
from collections import deque
lines = uf.read_lines("../input/10.in")
#lines = uf.read_lines("../tests/10.test")

lines = [[int(c) for c in line] for line in lines]

N = len(lines)
M = len(lines[0])

def dfs1(start):
    visited = set()
    count = 0
    stack = [start]
    visited.add(start)

    while stack:
        x, y = stack.pop()
        if lines[x][y] == 9:
            count += 1
            continue
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited:
                if lines[nx][ny] == lines[x][y] + 1:
                    visited.add((nx, ny))
                    stack.append((nx, ny))
    return count

def dfs2(start):
    count = 0
    stack = [start]
    while stack:
        x, y = stack.pop()
        if lines[x][y] == 9:
            count += 1
            continue
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and (nx, ny):
                if lines[nx][ny] == lines[x][y] + 1:
                    stack.append((nx, ny))
    return count

first = 0
second = 0
for i in range(N):
    for j in range(M):
        if lines[i][j] == 0:
            first += dfs1((i,j))
            second += dfs2((i,j))

print(first, second)