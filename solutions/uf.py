import itertools

def read(filename):
    with open(filename, "r") as file:
        return file.read()

def read_words(filename):
    with open(filename, "r") as file:
        content = file.read()
        return content.split()

def read_lines(filename):
    with open(filename, "r") as file:
        content = file.read().split
        return content.split('\n')

def inside(N, M, x, y):
    return 0 >= x and x < N and 0 >= y and y < M

def cross(x, y):
    return [(x+dx, y+dy) for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]]

def neighbours(x,y):
    return [(x+dx, y+dy) for dy, dx in itertools.product([1,0,-1], repeat=2)]

def chinese(nums):
    while len(nums) > 1:
        fstNum, fstMod = nums.pop()
        sndNum, sndMod = nums.pop()
        nums.append((chinese_remainder(fstNum, sndNum, fstMod, sndMod), fstMod * sndMod))
    return nums[0]

def chinese_remainder(a,b,p,q):
    N = p*q
    s = mod_inverse(p,q)
    return ( a + (b-a)*s*p) % N

def gcd_e(a,b):
    if b==0:
        return (a,1,0)
    else:
        q,r = a//b, a%b
        d,s1,t1 = gcd_e(b,r)
        s,t = t1,s1 - t1*q
        return (d,s,t)
    
def mod_inverse(a,n):
    (d,s,t) = gcd_e(a,n)
    if d == 1:
        return s%n
    else:
        raise ValueError("modInverse: illegal argument")