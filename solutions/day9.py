import uf
import copy 
def read(filename):
    with open(filename, "r") as file:
        return file.read().replace('\n', '')
    

#line = read("../tests/9.test")
line = read("../input/9.in")
first = []

i = 0
ident = 0
while i < len(line):
    if i % 2 == 0:
        for _ in range(int(line[i])):
            first.append(ident)
        ident += 1
    if i % 2 == 1:
        for _ in range(int(line[i])):
            first.append(-1)
    i += 1

second = copy.deepcopy(first)

k = 0
while True:
    last_elem = len(second) - 1
    while second[last_elem] == -1:
        last_elem -= 1
    first_free = 0
    while second[first_free] != -1:
        first_free += 1
    if first_free > last_elem:
        break
    item = second.pop(last_elem)
    second.pop(first_free)
    second.insert(first_free, item)
    k += 1


s = 0
for i in range(len(second)):
    if second[i] != -1:
        s += i * second[i]

print(s)

def getlastblock(l, i):
    while i >= 0 and l[i] == -1:
        i -= 1
    if i < 0:
        return -1, 0
    num = l[i]
    count = 1
    while i > 0 and l[i - 1] == num:
        count += 1
        i -= 1
    return i, count


def getfirstfree(l, size, s):
    i = 0
    while i < s:
        while i < s and l[i] != -1:
            i += 1
        if i >= s:
            return -1, -1
        j = i
        while j < s and l[j] == -1:
            j += 1
            if j - i == size:
                return i, j - i + 1
        i = j
    return -1, -1
    
fst = 0
last = len(first)
while True:
    if fst >= last:
        break
    last, blocklen = getlastblock(first, last - 1)
    fst, freelen = getfirstfree(first, blocklen, last)
    if blocklen <= freelen and first != -1 and last != -1:
        for i in range(blocklen):
            first[fst + i] = first[last + i]
            first[last + i] = -1
s = 0
for i in range(len(first)):
    if first[i] != -1:
        s += i * first[i]

print(s)



