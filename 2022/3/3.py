from string import ascii_letters

INPUT = 'input.txt'

priority = {letter: n for n,letter in enumerate(ascii_letters, start=1)}

if __name__=='__main__':
    #part 1
    priority_sum = 0
    with open(INPUT) as input_data:
        for line in input_data.readlines():
            total_length = len(line.strip())
            assert(total_length%2 == 0)
            half_length = total_length//2
            first_compartment  = line[:half_length]
            second_compartment = line[half_length:]
            for item in first_compartment:
                if item in second_compartment:
                    priority_sum += priority[item]
                    break

    print(f'Sum of the priorities of items in both compartments: {priority_sum}')

    #part 2
    priority_sum = 0
    with open(INPUT) as input_data:
        for n,line in enumerate(input_data.readlines()):
            if n%3 == 0:
                common_items = set(line.strip())
            else:
                common_items = [item for item in common_items if item in line.strip()]
            if n%3 == 2:
                assert(len(common_items)==1)
                priority_sum += priority[common_items[0]]

    print(f'Sum of the priorities of the badge-items: {priority_sum}')
