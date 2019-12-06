import sys

def parseInstruction(iPointer, list_):
    instr = int(list_[iPointer])
    loc1 = list_[iPointer + 1]
    loc2 = list_[iPointer + 2]
    loc3 = list_[iPointer + 3]
    if instr == 1:      # add
        res = list_[loc1] + list_[loc2]
        list_[loc3] = res
    elif instr == 2:    # multiply
        res = list_[loc1] * list_[loc2]
        list_[loc3] = res
    elif instr == 99:
        return -1
    else:
        return -2
    return iPointer + 4

def run(iPointer, mem, noun, verb):
    mem[1] = noun
    mem[2] = verb
    while 0 <= iPointer <= len(mem):
        iPointer = parseInstruction(iPointer, mem)
    #print(mem[0])
    return mem[0]

def main():
    file = open("input.txt")
    if len(sys.argv) <= 1:
        input_ = 19690720
    else:
        input_ = sys.argv[1]
    iPointer = 0
    line = file.readline()
    list_ = list(map(int, line.split(",")))
    for verb in range(0, 100):
        for noun in range(0, 100):
            #print("Values: {}, {}".format(verb, noun))
            b = list(map(int, line.split(",")))
            result = run(0, b, noun, verb)
            if result == int(input_):
                print("Values: {}, {}, {}".format(result, noun, verb))
                print("Result: {}".format((100*noun)+verb))
                return

main()
