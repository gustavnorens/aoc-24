import uf
import itertools

lines = uf.read_lines("../input/4.in")
#lines = uf.read_lines("../tests/4.test")


N = len(lines)
M = len(lines[0])

def search(x, y, dire):
    dx, dy = dire
    s = ""
    for i in range(4):
        nx, ny = x + i * dx, y + i * dy
        if not (0 <= nx < N and 0 <= ny < M):
            return False
        s += lines[nx][ny]
    return s == "XMAS"

def solve():
    first = 0
    second = 0
    for x in range(N):
        for y in range(M):
            for direction in itertools.product([-1, 0, 1], repeat=2):
                if search(x, y, direction):
                    first += 1
            if search3x3(x, y):
                print(x,y)
                second += 1
                
    return (first, second)


def search3x3(x, y):
    if not (1 <= x < N-1 and 1 <= y < M-1):
        return False
    
    count = 0
    s = ""
    s += lines[x-1][y-1]
    s += lines[x][y]
    s += lines[x+1][y+1]
    if s == "MAS":
        count += 1
    s = ""
    s += lines[x-1][y+1]
    s += lines[x][y]
    s += lines[x+1][y-1]
    if s == "MAS":
        count += 1
    s = ""
    s += lines[x+1][y+1]
    s += lines[x][y]
    s += lines[x-1][y-1]
    if s == "MAS":
        count += 1
    s = ""
    s += lines[x+1][y-1]
    s += lines[x][y]
    s += lines[x-1][y+1]
    if s == "MAS":
        count += 1
    return count >= 2
    

print(solve())

