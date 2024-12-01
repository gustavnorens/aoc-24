import uf


il = uf.read_lines("../input/1.in")
tl = uf.read_lines("../tests/1.test")

def solve1():
    s = 0
    t = 0 
    left = []
    right = []

    for line in il:
        (fst, snd) = line.split()
        fst = int(fst)
        snd = int(snd)
        left.append(fst)
        right.append(snd)
    left = sorted(left)
    right = sorted(right)
    
    final = [0] * len(left)


    for i in range(len(left)):
        s += abs(left[i] - right[i])


    for i in range(len(right)):
        final[i] = right.count(left[i])

    for i in range(len(left)):
        t += left[i] * final[i]

    print(s)
    print(t)

solve1()