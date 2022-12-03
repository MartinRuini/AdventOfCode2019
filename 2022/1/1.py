import numpy as np

INPUT = 'input.txt'

def calories_counter():
    calories = 0
    elf_idx  = 1
    with open(INPUT) as input_data:
        for line in input_data.readlines():
            if line.strip():
                calories += int(line.strip())
            else:
                yield elf_idx, calories
                calories = 0
                elf_idx += 1

if __name__=='__main__':
    # part 1
    max_calories = 0
    max_elf_idx  = 0
    for elf_idx, calories in calories_counter():
        if calories>max_calories:
            max_elf_idx, max_calories = elf_idx, calories
    print(f'elf number {max_elf_idx} is carrying the most calories: {max_calories}.')

    #part 2
    calories_1 = 0
    calories_2 = 0
    calories_3 = 0
    for elf_idx, calories in calories_counter():
        if calories>calories_1:
            calories_1, calories_2, calories_3 = calories, calories_1, calories_2
        elif calories>calories_2:
            calories_2, calories_3 = calories, calories_2
        elif calories>calories_3:
            calories_3 = calories
    top3calories = calories_1 + calories_2 + calories_3
    print(f'The three Elves with the most calories carry together {top3calories} calories')
