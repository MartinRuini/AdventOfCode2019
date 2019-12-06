def manhattan(intersections):
    distances = []
    for el in intersections:
        distance = abs(int(el[0])) + abs(int(el[1]))
        distances.append(distance)
    return distances


def findIntersection(paths):
    intersections = []
    for index, pos in enumerate(paths[0]):
        if index % 1000 == 0:
            print(index)
        if pos in paths[1]:
            intersections.append(pos)
    return intersections

def parsePath(wires):
    paths = []
    #print("Direction: {}\nValue: {}".format(wires[0][0][0], wires[0][0][1:]))

    for path in wires:
        position = [0, 0]
        tmpPath = []
        for el in path:
            direction = el[0]
            value = int(el[1:])
            while value > 0:
                #print(value)
                if direction == "R":
                    position[0] = position[0] + 1
                elif direction == "L":
                    position[0] = position[0] - 1
                elif direction == "U":
                    position[1] = position[1] + 1
                elif direction == "D":
                    position[1] = position[1] - 1
                tmpPos = []
                tmpPos.extend(position)
                tmpPath.append(tmpPos)
                #print(len(tmpPath))
                value = value - 1
            #print(tmpPath)
        paths.append(tmpPath)
    return paths

def getInput():
    wires = []
    for index, line in enumerate(open("input.txt").readlines()):
        wires.insert(index, line.split(","))
    return wires

def main():
    wires = getInput()
    paths = parsePath(wires)
    #print(findIntersection(paths))
    intersections = findIntersection(paths)
    print(intersections)
    mnht = manhattan(intersections)
    print(mnht)
    print(min(mnht))
main()
