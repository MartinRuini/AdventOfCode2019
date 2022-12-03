def parseInstruction(value):
    value = str(value)
    c = 1
    m = value[:-2]
    instr = int(value[-2:])
    modes = []

    while c <= 3:
        if len(m) - c < 0:
            modes.append(0)
        else:
            modes.append(int(m[len(m) - c]))
        c = c + 1

    return modes, instr

print(parseInstruction(9))