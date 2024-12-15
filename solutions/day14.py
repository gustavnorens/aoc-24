import uf

N = 103
M = 101

lines = uf.read_lines("../input/14.in")  

inputs = []
for line in lines:
    left, right = line.split()
    x,y = list(map(int, left[2:].split(",")))
    dx,dy = list(map(int, right[2:].split(",")))
    inputs.append((x,y,dx,dy))

def simulate(x, y, dx, dy, sims):
    y = (y + dy * sims) % N
    x = (x + dx * sims) % M
    ret = -1
    if x < M // 2 and y < N // 2:
        ret = 0
    if x > M // 2 and y < N // 2:
        ret =  1
    if x > M // 2 and y > N // 2:
        ret = 2
    if x < M // 2 and y > N // 2:
        ret = 3
    return ret, (x,y)

def count_neigh(robots):
    biggest = 0
    for robot in robots:
        start = [robot]
        visited = set()
        while start:
            curr = start.pop()
            if curr in visited:
                break
            visited.add(curr)
            for pair in uf.neighbours(*curr):
                if pair in robots:
                    start.append(pair)
        if len(visited) > biggest:
            biggest = len(visited)
    return biggest

def part1(inputs):
    nums = [0,0,0,0,0]
    for (x,y,dx,dy) in inputs:
        nums[simulate(x,y,dx,dy, 100)[0]] += 1
    tot = 1
    for num in nums[:-1]:
        tot *= num
    return tot

def part2(inputs):
    biggest = 0
    second = 0
    for k in range(10000):
        robots = set()
        for x,y,dx,dy in inputs:
            robots.add(simulate(x,y,dx,dy,k)[1])
        res = count_neigh(robots)
        if res > biggest:
            biggest = res
            second = k
    return second
    
print(part1(inputs), part2(inputs))