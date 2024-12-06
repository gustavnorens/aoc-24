import uf

lines = uf.read_lines("../input/6.in")
#lines = uf.read_lines("../tests/6.test")

def newDir(dx,dy):
    if (dx, dy) == (1,0):
        return (0,-1)
    if (dx, dy) == (0,-1):
        return (-1,0)
    if (dx, dy) == (-1,0):
        return (0,1)
    if (dx, dy) == (0,1):
        return (1,0)
    
def stuck(x,y, dx, dy):
    seen = set()
    while x >= 0 and x < N and y >= 0 and y < M:
        if (x,y,dx,dy) in seen:
            return True
        seen.add((x,y,dx,dy))
        nx,ny = x + dx, y + dy
        if not (nx >= 0 and nx < N and ny >= 0 and ny < M):
            return False
        if lines[nx][ny] == "#":
            dx,dy = newDir(dx,dy)
        else:
            x,y = nx, ny
    return False

seen = set()

N = len(lines)
M = len(lines[0])

direction = 0

for i in range(N):
    for j in range(M):
        if lines[i][j] == ">":
            pos = i,j
            direction = 0,1
        if lines[i][j] == "<":
            pos = i,j
            direction = 0,-1
        if lines[i][j] == "^":
            pos = i,j
            direction = -1,0
        if lines[i][j] == "v":
            pos = i,j
            direction = 1,0

lines = [list(s) for s in lines]
count = 0
print(N,M)
x,y = pos
dx, dy = direction
seen.add((x,y))
for i in range(N):
    for j in range(M):
        if lines[i][j] == ".":
            print(i,j)
            lines[i][j] = '#'
            if stuck(x,y,dx,dy):
                count += 1
            lines[i][j] = "."




print(count)


