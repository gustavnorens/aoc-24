import uf
import copy
from collections import defaultdict
lines = uf.read("../input/11.in")
#lines = uf.read("../tests/11.test")

#lines = [[int(c) for c in line] for line in lines]


lines = list(map(int,lines.split()))
f = defaultdict(int)
s = defaultdict(int)
for num in lines:
    f[0, num] = lines.count(num)
    s[0, num] = lines.count(num)

def apply(num, dick):
    for i in range(num):
        for (i, stone), count in list(dick.items()): 
            if stone == 0:
                dick[i+1, 1] += count
            elif len(str(stone)) % 2 == 0:
                k = len(str(stone)) // 2
                left = int(str(stone)[:k])
                right = int(str(stone)[k:])
                dick[i + 1, left] += count
                dick[i + 1, right] += count
            else:
                dick[i + 1, stone * 2024] += count
                
first = 25
second = 75
apply(first, f)
apply(second,s)
print(sum([f[first,num] for blink, num in f.keys() if blink == first]))
print(sum([s[second, num] for blink, num in s.keys() if blink == second]))





