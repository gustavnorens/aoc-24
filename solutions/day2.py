import uf
import copy

il = uf.read_lines("../input/2.in")
tl = uf.read_lines("../tests/2.test")

def solve():
    one = 0
    two = 0

    for line in il:
        res = list(map(int, line.split()))
        if b(res):
            one += 1
            two += 1
        elif any(map(b,sublists(res))):
            two += 1
        
    return (one, two)

def b(l):
    return (inc(l) or dec(l)) and close(l)

def sublists(l):
    new = []
    for i in range(len(l)):
        c = copy.deepcopy(l)
        c.pop(i)
        new.append(c)
    return new

def close(lst):
    return all(1 <= abs(lst[i] - lst[i + 1]) <= 3 for i in range(len(lst) - 1))
    
def inc(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

def dec(lst):
    return all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))


print(solve())
