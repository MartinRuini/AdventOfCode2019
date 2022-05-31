import numpy as np

def main():
    inFile = 'input.txt'
    with open(inFile) as f:
        data = [line.strip() for line in f.readlines()]

    ### part 1
    horizontalPosition, depth = 0, 0
    for step in data:
        direction, value = step.split(' ')
        if direction=='forward':
            horizontalPosition += int(value)
        elif direction=='down':
            depth += int(value)
        elif direction=='up':
            depth -= int(value)
        else:
            print(f'Cannot parse "{step}"')
    print(horizontalPosition*depth)

    ### part 2
    horizontalPosition, depth, aim = 0, 0, 0
    for step in data:
        direction, value = step.split(' ')
        value = int(value)
        if direction=='forward':
            horizontalPosition += value
            depth += aim*value
        elif direction=='down':
            aim += value
        elif direction=='up':
            aim -= value
        else:
            print(f'Cannot parse "{step}"')
    print(horizontalPosition*depth)

if __name__=='__main__':
    main()
