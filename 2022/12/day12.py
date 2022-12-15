import numpy as np
from string import ascii_lowercase
from matplotlib import pyplot as plt

INPUT = 'input.txt'

class PathFinder():
    def __init__(self, input_file):
        self.height_map = np.genfromtxt(input_file, dtype=str, delimiter=1)
        self.elevation  = np.zeros_like(self.height_map, dtype=int)
        for n, char in enumerate(ascii_lowercase):
            self.elevation[ self.height_map==char ] = n
        self.elevation[ self.height_map=='S' ] = 0
        self.elevation[ self.height_map=='E' ] = n
        (self.start_x,), (self.start_y,) = np.where(self.height_map=='S')
        (self.end_x,),   (self.end_y,)   = np.where(self.height_map=='E')
        self.reset()

    def reset(self):
        self.paths   = [[(self.end_x,self.end_y)]]
        self.visited = np.zeros_like(self.height_map, dtype=bool)
        self.visited[ self.height_map=='E' ] = True

    def find_valid_neighbours(self, x, y):
        z = self.elevation[x,y]
        neighbours = []
        if x>0:
            left_neighbour = (x-1, y)
            neighbours += [left_neighbour]
        if y>0:
            above_neighbour = (x, y-1)
            neighbours += [above_neighbour]
        x_max, y_max = self.elevation.shape
        if x<x_max-1:
            right_neighbour = (x+1, y)
            neighbours += [right_neighbour]
        if y<y_max-1:
            below_neighbour = (x,y+1)
            neighbours += [below_neighbour]
        for neighbour in neighbours:
            if (self.elevation[neighbour] >= z-1) and not self.visited[neighbour]:
                self.visited[neighbour] = True
                yield neighbour

    def extend_paths(self):
        for _ in range(len(self.paths)):
            path = self.paths.pop(0)
            for neighbour in self.find_valid_neighbours(*path[-1]):
                    self.paths.append([path[-1],neighbour])

    def find_shortest_path(self, part):
        self.reset()
        path_length_counter = 0
        while True:
            self.extend_paths()
            if not self.paths: #if no paths are left, i.e all dead ends
                return np.inf
            path_length_counter += 1
            if part==1:
                condition = any(path[-1]==(self.start_x,self.start_y) for path in self.paths)
            elif part==2:
                condition = any(self.elevation[path[-1]]==0 for path in self.paths)
            else:
                raise ValueError(f'Unknown part {part}')

            if condition:
                #plt.imshow(self.visited)
                #plt.show()
                return path_length_counter



def main():
    path_finder = PathFinder(INPUT)

    #part 1
    shortest_path = path_finder.find_shortest_path(1)
    print(f'Part 1 {shortest_path = }')

    #part 2
    shortest_path = path_finder.find_shortest_path(2)
    print(f'Part 2 {shortest_path = }')

if __name__=='__main__':
    main()
