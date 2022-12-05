INPUT = 'input.txt'

def parse_starting_stacks(starting_stacks):
    stacks = [ [] for _ in starting_stacks[-1][1::4]]
    for line in starting_stacks[-2::-1]:
        for crate,stack in zip(line[1::4], stacks):
            if crate!=' ':
                stack += [crate]
    return stacks

def move_crates_part_1(stacks, from_stack, to_stack, number):
    for _ in range(number):
        stacks[to_stack] += stacks[from_stack].pop()
    return stacks

def move_crates_part_2(stacks, from_stack, to_stack, number):
    stacks[to_stack] += stacks[from_stack][-number:]
    del stacks[from_stack][-number:]
    return stacks

def parse_instruction(line):
    instruction_words = line.split(' ')
    number_of_crates  = int(instruction_words[1])
    from_stack        = int(instruction_words[3])-1
    to_stack          = int(instruction_words[5])-1
    return (from_stack, to_stack, number_of_crates)

def main():
    starting_stacks = []
    reading_stacks  = True
    with open(INPUT) as input_data:
        for line in input_data.readlines():
            line = line.strip('\n')
            if line=='': continue
            if reading_stacks:
                starting_stacks += [line]
                if line.strip().startswith('1'):
                    reading_stacks = False
                    stacks_part_1 = parse_starting_stacks(starting_stacks)
                    stacks_part_2 = parse_starting_stacks(starting_stacks)
            else:
                instructions = parse_instruction(line)
                stacks_part_1 = move_crates_part_1(stacks_part_1, *instructions)
                stacks_part_2 = move_crates_part_2(stacks_part_2, *instructions)
    #for stacks in (stacks_part_1, stacks_part_2):
    #    for stack in stacks:
    #        print(''.join(stack))
    #    print()
    print(f'Part 1: {"".join(stack[-1] for stack in stacks_part_1)}')
    print(f'Part 2: {"".join(stack[-1] for stack in stacks_part_2)}')

if __name__=='__main__':
    main()
