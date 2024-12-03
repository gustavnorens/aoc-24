import uf

inputfile = "../input/3.in"
testfile = "../tests/3.test"
lines = uf.read_lines(inputfile)
#lines = uf.read_lines(testfile)

#lines = ["do() don't() mul(2,3)"]

def parse(s):
    on = True
    t = 0
    for i in range(len(s)):
        (fst, snd) = onCheck(s[i:])
        if fst:
            on = snd
        (b1, s1) = parseMul(s[i:])
        if b1:
            (b2, s2, left) = parseNum(s1)
            if b2:
                (b3, s3) = parseComma(s2)
                if b3:
                    (b4, s4, right) = parseNum(s3)
                    if b4:
                        (b5, _) = parseParen(s4)
                        if b5 and on:
                            
                            t += left * right
    return t



def parseMul(s):
    if s[:4] == "mul(":
        return (True, s[4:])
    return (False, "")
        
def parseNum(s):
    if s[:3].isdigit():
        return (True,  s[3:],int(s[:3]))
    elif s[:2].isdigit():
        return (True, s[2:],int(s[:2]))
    elif s[:1].isdigit():
        return (True, s[1:],int(s[:1]))
    return (False, "", 0)

def parseComma(s):
    if s[0] == ",":
        return (True, s[1:])
    return (False, "")

def parseParen(s):
    if s[0] == ")":
        return (True, s[1:])
    return (False, "")

def onCheck(s):
    if s[:4] == "do()":
        return (True, True)
    elif s[:7] == "don't()":
        return (True,False)
    return (False, False)


print(sum(list(map(parse, lines))))