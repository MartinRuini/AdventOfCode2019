import numpy as np

INPUT = 'input.txt'

class Rope():
    def __init__(self, length=10, start_x=0, start_y=0):
        self.length = length
        for i in range(self.length):
            setattr(self, f'knot{i}_x', start_x)
            setattr(self, f'knot{i}_y', start_y)
        self.tail_trail = [(start_x, start_y)]

    def move_head(self, direction, nsteps):
        for _ in range(nsteps):
            if direction=='R':
                self.knot0_x += 1
            elif direction=='U':
                self.knot0_y += 1
            elif direction=='L':
                self.knot0_x -= 1
            elif direction=='D':
                self.knot0_y -= 1
            self._move_body()

    def _move_body(self):
        for i in range(self.length-1):
            delta_x = getattr(self, f'knot{i}_x') - getattr(self, f'knot{i+1}_x')
            delta_y = getattr(self, f'knot{i}_y') - getattr(self, f'knot{i+1}_y')
            if abs(delta_x)+abs(delta_y)>2:
                setattr(self, f'knot{i+1}_x', getattr(self, f'knot{i+1}_x')+np.sign(delta_x))
                setattr(self, f'knot{i+1}_y', getattr(self, f'knot{i+1}_y')+np.sign(delta_y))
            else:
                if abs(delta_x)>1:
                    setattr(self, f'knot{i+1}_x', getattr(self, f'knot{i+1}_x')+np.sign(delta_x))
                if abs(delta_y)>1:
                    setattr(self, f'knot{i+1}_y', getattr(self, f'knot{i+1}_y')+np.sign(delta_y))
        tail_position = (getattr(self, f'knot{i+1}_x'), getattr(self, f'knot{i+1}_y'))
        if tail_position not in self.tail_trail:
            self.tail_trail += [tail_position]

def main():
    rope_part1 = Rope(length=2)
    rope_part2 = Rope(length=10)
    with open(INPUT) as input_data:
        for line in input_data.readlines():
            direction, nsteps = line.strip().split(' ')
            nsteps = int(nsteps)
            rope_part1.move_head(direction, nsteps)
            rope_part2.move_head(direction, nsteps)
    n_tail_positions_part1 = len(rope_part1.tail_trail)
    n_tail_positions_part2 = len(rope_part2.tail_trail)
    print(f'{n_tail_positions_part1 = }')
    print(f'{n_tail_positions_part2 = }')

if __name__=='__main__':
    main()
