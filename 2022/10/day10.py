import numpy as np
import matplotlib.pyplot as plt

INPUT = 'input.txt'
SCREEN_WIDTH  = 40
SCREEN_HEIGHT = 6

def draw_pixel(X, cycle_counter, screen):
    pixel_x, pixel_y = cycle_counter%SCREEN_WIDTH, cycle_counter//SCREEN_WIDTH
    if abs(pixel_x-X)<2:
        screen[pixel_y, pixel_x] = True
    return screen

def parse_input(yield_at, screen):
    X = 1
    cycle_counter = 0
    yield_counter = 0
    with open(INPUT) as input_data:
        for line in input_data.readlines():
            if line.startswith('noop'):
                screen = draw_pixel(X, cycle_counter, screen)
                cycle_counter += 1
                if yield_counter<len(yield_at) and cycle_counter == yield_at[yield_counter]:
                    yield yield_at[yield_counter] * X
                    yield_counter += 1
            elif line.startswith('addx'):
                for _ in range(2):
                    screen = draw_pixel(X, cycle_counter, screen)
                    cycle_counter += 1
                    if yield_counter<len(yield_at) and cycle_counter == yield_at[yield_counter]:
                        yield yield_at[yield_counter] * X
                        yield_counter += 1
                X += int( line.strip().split(' ')[1] )

def main():
    yield_at_cycle = [20+i*40 for i in range(6)]
    screen = np.zeros((SCREEN_HEIGHT,SCREEN_WIDTH), dtype=bool)

    signal_strengths = list(parse_input(yield_at_cycle, screen))
    for cycle, signal_strength in zip(yield_at_cycle, signal_strengths):
        print(f'{cycle = }, {signal_strength = }')
    sum_of_signal_strengths = sum(signal_strengths)
    print(f'{sum_of_signal_strengths = }')
    plt.imshow(screen)
    plt.show()

if __name__=='__main__':
    main()
