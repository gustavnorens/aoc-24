import uf
from collections import defaultdict

lines = uf.read("../input/13.in")
#lines = uf.read("../tests/13.test")


#grid = [[c for c in line] for line in lines]

lines = lines.split("\n\n")

def possible(a1, a2, b1, b2, p1, p2, num):
    y = (a1 * (p2 + num) - a2 * (p1 + num) ) / (a1*b2-a2*b1)
    x = ((p1 + num)-b1*y) / a1
    if x.is_integer() and y.is_integer():
        return (3*int(x) + int(y))
    return 0

first = 0
second = 0
for puzzel in lines:
    puzzel = puzzel.split()
    A = (int(puzzel[2][2:-1]), int(puzzel[3][2:]))
    B = (int(puzzel[6][2:-1]), int(puzzel[7][2:]))
    price = (int(puzzel[-2][2:-1]), int(puzzel[-1][2:]))
    first += possible(*A,*B,*price, 0)
    second += possible(*A,*B,*price, 10000000000000)
print(first, second)