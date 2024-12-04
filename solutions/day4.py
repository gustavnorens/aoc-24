import uf
import itertools

lines = uf.read_lines("../input/4.in")
#lines = uf.read_lines("../tests/4.test")


N = len(lines)
M = len(lines[0])

def findXMAS(x, y, dire):
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
                if findXMAS(x, y, direction):
                    first += 1
            if findMAS(x, y):
                second += 1
                
    return (first, second)


def findMAS(x, y):
    count = 0
    for i,j in itertools.product([-1,1], repeat=2):
        dx, dy = -i, -j
        s = ""
        for k in range(3):
            nx, ny = x + i + dx * k, y + j + dy * k
            if not (0 <= nx < N and 0 <= ny < M):
                return False
            s += lines[nx][ny]
        if s == "MAS":
            count += 1
    return count >= 2
    

print(solve())

