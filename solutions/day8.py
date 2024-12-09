import uf 

lines = uf.read_lines("../input/8.in")
#lines = uf.read_lines("../tests/8.test")

def inside(x,y):
    return x >= 0 and x < N and y >= 0 and y < M

def get_antinodes(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    l = []

    for i in range(-100, 100):
        l.append((x1 - dx * i, y1 - dy * i))  
        l.append((x2 + dx * i, y2 + dy * i))
        if i == 1:
            fst = x1 - dx, y1 - dy 
            snd = x2 + dx, y2 + dy

    return [fst, snd], l 

N = len(lines)
M = len(lines[0])

d = {key: [] 
     for key in 
     [chr(i) for i in range(97, 123)] + 
     [chr(i) for i in range(65, 91)] + 
     [chr(i) for i in range(48, 58)]}

for i in range(N):
    for j in range(M):
        if lines[i][j] in d:
            d[lines[i][j]].append((i,j))

first = set()
second = set()

for key, cords in d.items():
    for i in range(len(cords)):
        for j in range(i+1, len(cords)):
            fst, snd = get_antinodes(*cords[i], *cords[j])
            for antinode in fst:
                if inside(*antinode):
                    first.add(antinode)
            for antinode in snd:
                if inside(*antinode):
                    second.add(antinode)
        
print(len(first), len(second))

