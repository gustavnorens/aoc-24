import uf

lines = uf.read("../input/15.in")  
#lines = uf.read("../tests/15.test")  

grid, seq = lines.split("\n\n")
grid = [list(line) for line in grid.split("\n")]

seq = seq.replace("\n", "")
newgrid = []
for line in grid:
    row = []
    for c in line:
        if c == ".":
            row.append(".")
            row.append(".")
        if c == "#":
            row.append("#")
            row.append("#")
        if c == "O":
            row.append("[")
            row.append("]")
        if c == "@":
            row.append("@")
            row.append(".")
    newgrid.append(row)


def moveHorizontal(grid, x, y, dx, dy): 
    N, M = len(grid), len(grid[0])
    nx, ny = x + dx, y + dy
    if nx >= 0 and nx < N and ny >= 0 and ny < M:
        if grid[nx][ny] == ".":
            grid[nx][ny] = grid[x][y]
            return True
        elif grid[nx][ny] == "[" or grid[nx][ny] == "]" or grid[nx][ny] == "O":
            if moveHorizontal(grid, nx, ny, dx, dy):
                grid[nx][ny] = grid[x][y]
                return True
    return False

def shouldMove(grid, nx, ny, dx):
    if grid[nx][ny] == ".":
        return True
    elif grid[nx][ny] == "[":
        return shouldMove(grid, nx+dx, ny, dx) and shouldMove(grid, nx+dx, ny+1, dx)
    elif grid[nx][ny] == "]":
        return shouldMove(grid, nx+dx, ny, dx) and shouldMove(grid, nx+dx, ny-1, dx)
    return False 

def move(grid, x, y, dx):
    nx,ny = x+dx, y
    if grid[x][y] == "[":
        move(grid,nx,ny,dx)
        move(grid,nx,ny + 1,dx)
        grid[nx][ny] = grid[x][y]
        grid[nx][ny + 1] = grid[x][y+1]
        grid[x][y] = "."
        grid[x][y+1] = "."
    elif grid[x][y] == "]":
        move(grid,nx,ny,dx)
        move(grid,nx,ny -1,dx)
        grid[nx][ny] = grid[x][y]
        grid[nx][ny - 1] = grid[x][y-1]
        grid[x][y] = "."
        grid[x][y-1] = "."

def moveVertical(grid, x, y, dx, dy):
    N, M = len(grid), len(grid[0])
    nx, ny = x + dx, y + dy
    if nx >= 0 and nx < N and ny >= 0 and ny < M:
        if shouldMove(grid, nx,ny, dx):
            move(grid, nx, ny, dx)
            return True
    return False

def getStart(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                #grid[i][j] = "."
                return (i,j)
            
def solve(grid, x, y, vertical, horizontal):
    N, M = len(grid), len(grid[0])
    directions = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
    for direction in seq.strip():
        grid[x][y] = "."
        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if grid[nx][ny] == ".":
                x, y = nx, ny
            elif grid[nx][ny] == "[" or grid[nx][ny] == "]" or grid[nx][ny] == "O":
                if (dx,dy) == (1,0) or (dx,dy) == (-1,0):
                    if vertical(grid, x, y, dx, dy):
                        x, y = nx, ny
                else:
                    if horizontal(grid, x, y, dx,dy):
                        x,y = nx,ny
        
        grid[x][y] = "@"
    return grid
def getScore(grid, c):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == c:
                count += 100 * i + j
    return count

grid = solve(grid, *getStart(grid), moveHorizontal, moveHorizontal)
newgrid = solve(newgrid, *getStart(newgrid), moveVertical, moveHorizontal)
first = getScore(grid, "O")
second = getScore(newgrid, "[")
print(first, second)
