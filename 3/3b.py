def manhattan(intersections):
    distances = []
    for el in intersections:
        distance = abs(int(el[0])) + abs(int(el[1]))
        distances.append(distance)
    return distances

def shortestPath(intersections, paths):
    steps = []
    for el in intersections:
        count1 = 1
        count2 = 1
        for pos in paths[0]:
            if el != pos:
                count1 = count1 + 1
            else:
                break
        for pos in paths[1]:
            if el != pos:
                count2 = count2 + 1
            else:
                break
        steps.append(count1 + count2)
    return min(steps)



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


    """intersections = findIntersection(paths)
    mnht = manhattan(intersections)
    print(shortestPath(intersections, paths))
    print(intersections)"""


    file = open("intersections.txt").readlines()
    lll = []
    for el in file:
        ele = el.split(",")
        ele[1] = ele[1].strip()
        ele[0] = int(ele[0])
        ele[1] = int(ele[1])
        lll.append(ele)
    #print(lll)
    print(shortestPath(lll, paths))
main()
