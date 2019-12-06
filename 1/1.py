def fuel():
    file = open("input.txt")
    res = 0
    for el in file.readlines():
        res = res + (int(el)//3)-2
    return res

print(fuel())

