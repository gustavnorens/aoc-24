import uf

lines = uf.read_lines("../input/17.in")  
#lines = uf.read_lines("../tests/17.test")  


registers = []
for i in range(3):
    registers.append(int(lines[i].split(" ")[2]))
program = list(map(int,lines[-1].split(" ")[1].split(",")))

def combo(value, registers):
    if 0 <= value <= 3:
        return value
    if 4 <= value <= 6:
        return registers[value-4]
    return "problem"

def updateRegisters(opcode, operand, registers):
        if opcode == 0:
            registers[0] = int(registers[0] / (2 ** combo(operand, registers)))
        elif opcode == 1:
            registers[1] = registers[1] ^ operand
        elif opcode == 2:
            registers[1] = combo(operand, registers) % 8
        elif opcode == 4:
            registers[1] = registers[1] ^ registers[2]
        elif opcode == 6:
            registers[1] = int(registers[0] / (2 ** combo(operand, registers)))
        elif opcode == 7:
            registers[2] = int(registers[0] / (2 ** combo(operand, registers)))
        return registers

def evaluate(program, registers):
    i = 0
    result = []
    while 0 <= i < len(program):
        if program[i] == 5:
            result.append(combo(program[i+1], registers) % 8)
            i += 2
        elif program[i] == 3:
            if registers[0] != 0:
                i = combo(program[i + 1], registers)
            else:
                i += 2
        else:
            registers = updateRegisters(program[i], program[i + 1], registers)
            i += 2
    return result

def get_b_from_a(A):
    B = A & 7
    B = B ^ 1
    C = int(A / 2**B)
    B = B ^ C
    A = int(A / 8)
    return (B ^ 4) % 8

def p2(program):
    nums = range(1,8)
    for i in range(len(program) - 1, 0, -1):
        new = []
        for num in nums:
            if get_b_from_a(num) == program[i]:
                new.extend(range(num * 8, num * 8 + 8))
        nums = new
    return min(num for num in nums if get_b_from_a(num) == program[0])
print(",".join(map(str,evaluate(program, registers))))
print(p2(program))
