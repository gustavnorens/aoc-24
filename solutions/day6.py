import uf
import itertools

lines = uf.read_lines("../input/6.in")
#lines = uf.read_lines("../tests/6.test")

def simulate(x,y):
    seen = set()
    dirs = itertools.cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])
    dx, dy = dirs.__next__()
    while x >= 0 and x < N and y >= 0 and y < M:
        if (x,y,dx,dy) in seen:
            return True, 0
        seen.add((x,y,dx,dy))
        nx,ny = x + dx, y + dy
        if not (nx >= 0 and nx < N and ny >= 0 and ny < M):
            return False, seen
        if lines[nx][ny] == "#":
            dx,dy = dirs.__next__()
        else:
            x,y = nx, ny
    return False, seen


N = len(lines)
M = len(lines[0])
lines = [list(s) for s in lines]
count = 0

for i in range(N):
    for j in range(M):
        if lines[i][j] in "><^v":
            pos = i,j

for i in range(N):
    for j in range(M):
        if lines[i][j] == ".":
            lines[i][j] = '#'
            if simulate(*pos)[0]:
                count += 1
            lines[i][j] = "."

print(len(set([(x,y) for (x,y,_,_) in simulate(*pos)[1]])), count)