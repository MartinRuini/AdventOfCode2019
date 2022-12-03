def fetchInstruction(iPointer, list_):
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

def main():
    file = open("input.txt")
    iPointer = 0
    list_ = list(map(int, file.readline().split(",")))
    list_[1] = 12
    list_[2] = 2
    while iPointer >= 0 and iPointer <= len(list_):
        iPointer = fetchInstruction(iPointer, list_)
    if iPointer == -1:
        print("Run terminated successfully.")
    elif iPointer == -2:
        print("An error occurred!")
    print(list_[0])


main()
