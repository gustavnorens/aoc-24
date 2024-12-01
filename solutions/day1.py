import uf


il = uf.read_lines("../input/1.in")
tl = uf.read_lines("../tests/1.test")

def solve1():
    s = 0
    t = 0 
    left = []
    right = []

    for line in il:
        (fst, snd) = map(int, line.split())
        left.append(fst)
        right.append(snd)

    left = sorted(left)
    right = sorted(right)

    for i in range(len(right)):
        t += right.count(left[i]) * left[i]
        s += abs(left[i] - right[i])

    print(s)
    print(t)

solve1()