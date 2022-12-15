import numpy as np
from string import ascii_lowercase
import multiprocessing
from time import perf_counter
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

    def find_shortest_path(self, start_xy=None):
        self.reset()
        if start_xy is None:
            start_x = self.start_x
            start_y = self.start_y
        else:
            start_x, start_y = start_xy
        path_length_counter = 0
        while True:
            #if path_length_counter%100==0:
            #    plt.imshow(self.visited)
            #    plt.show()
            self.extend_paths()
            if not self.paths: #if no paths are left, i.e all dead ends
                return np.inf
            path_length_counter += 1
            if any(path[-1]==(start_x,start_y) for path in self.paths):
                return path_length_counter


def main():
    #part 1
    tstart = perf_counter()
    path_finder = PathFinder(INPUT)
    shortest_path = path_finder.find_shortest_path()
    tstop = perf_counter()
    print(f'Part 1 {shortest_path = }, time = {tstop-tstart:.2f}')

    #part 2
    tstart = perf_counter()
    distances = map(path_finder.find_shortest_path, zip(*np.where(path_finder.elevation==0)))
    shortest_path = min(distances)
    tstop = perf_counter()
    print(f'No multiprocessing Part 2 {shortest_path = }, time = {tstop-tstart:.2f}')

    tstart = perf_counter()
    with multiprocessing.Pool() as pool:
        distances = pool.map(path_finder.find_shortest_path, zip(*np.where(path_finder.elevation==0)))
    shortest_path = min(distances)
    tstop = perf_counter()
    print(f'w/ multiprocessing Part 2 {shortest_path = }, time = {tstop-tstart:.2f}')


if __name__=='__main__':
    main()
