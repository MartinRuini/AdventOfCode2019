class Node:
    def __init__(self, name, orbits):
        self.name = name
        self.orbits = orbits
        self.value = 0

    def __str__(self):
        return f'Name: {self.name} is orbited by: {self.orbits}'


def count(nodes, start):
    counting_set = [start]
    tmp = []
    round = 0
    result = 0
    while len(counting_set) > 0:
        for el in nodes:
            if el.name in counting_set:
                result = result + round
                tmp.append(el.orbits)

                counting_set = []
                counting_set.extend(tmp)
                tmp = []
                round = round + 1
                print(f'Round: {round}, {counting_set}')

    return result


def parseInput():
    nodes = []
    file = open("input.txt").readlines()
    for el in file:
        couple = el.split(")")
        new_node = Node(couple[0].strip(), couple[1].strip())
        nodes.append(new_node)
    for el in nodes:
        for el2 in nodes:
            if el.orbits == el2.name:
                el.pointer = el2
    print(count(nodes, "COM"))
    return nodes

parseInput()
