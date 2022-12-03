def recFuel(mass):
    if mass <= 0:
        return 0
    else:
        return mass + recFuel((mass//3)-2)

def fuel():
    file = open("input.txt")
    res = 0
    for el in file.readlines():
        res = res + recFuel(int(el))
        res = res - int(el)
    return res


print(fuel())
