import uf

lines = uf.read_lines("../input/5.in")
#lines = uf.read_lines("../tests/5.test")

rules = []

updates = []

d = {}

for line in lines:
    if '|' in line:
        rules.append(list(map(int, line.split("|"))))
    elif line == "":
        ...
    else:
        updates.append(list(map(int, line.split(","))))


d = {left: [] for (left, _) in rules}

for (left, right) in rules:
    if left in d.keys():
        d[left].append(right)

def solve(nums):
    for i in range(len(nums)):
        if nums[i] in d:
            for right in d[nums[i]]:
                if right in nums and right in nums[:i]:
                    return False
    return True

def fix(nums):
    topo = {num: [] for num in nums}
    bad = {num: 0 for num in nums}

    for left in nums:
        if left not in d:
            continue
        for right in d[left]:
            if right in nums:
                topo[left].append(right)
                bad[right] += 1

    good = [num for num in nums if bad[num] == 0]
    result = []

    while good:
        remove = good.pop()
        result.append(remove)
        for node in topo[remove]:
            bad[node] -= 1
            if bad[node] == 0:
                good.append(node)

    return result

first = 0
second = 0
for update in updates:
    if solve(update):
        first += update[len(update) // 2]
    else:
        update = fix(update)
        second += update[len(update) // 2]
print(first, second)
