import uf
import itertools
import copy

lines = uf.read_lines("../input/7.in")
#lines = uf.read_lines("../tests/7.test")

def possible(val, nums):
    addmul, concat = zip(*[evals(nums, ops) for ops in itertools.product("+*|", repeat=len(nums) - 1)])
    fun = lambda num: num == val
    return any(map(fun, addmul)), any(map(fun, concat))
        

def evals(nums, ops):
    addmul = copy.deepcopy(nums)
    concat = copy.deepcopy(nums)
    i = 0
    for op in ops:
        if op == '+':
            concat[i + 1] = concat[i] + concat[i+1]
            addmul[i + 1] = addmul[i] + addmul[i+1]
            i += 1
        elif op == '*':
            concat[i + 1] = concat[i] * concat[i+1]
            addmul[i + 1] = addmul[i] * addmul[i+1]
            i += 1
        elif op == '|':
            concat[i + 1] = int(str(concat[i]) + str(concat[i+1]))
            i += 1
    return (addmul[i], concat[i])

first = 0
second = 0
for line in lines:
    (fst, rest) = line.split(": ")
    value, nums = int(fst), list(map(int, rest.split()))
    if possible(value, nums)[0]:
        first += value
    if possible(value, nums)[1]:
        second += value

print(first, second)