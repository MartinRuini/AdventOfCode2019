INPUT = 'input.txt'

def main():
    complete_overlaps = 0
    #partial_overlaps_strict  = 0
    partial_overlaps = 0
    with open(INPUT) as input_data:
        for line in input_data.readlines():
            first_assignment, second_assignment = line.strip().split(',')
            first_assignment_start, first_assignment_stop = map(int, first_assignment.split('-'))
            second_assignment_start, second_assignment_stop = map(int, second_assignment.split('-'))

            #part 1
            if ((first_assignment_start <= second_assignment_start) and (first_assignment_stop >= second_assignment_stop)) or ((second_assignment_start <= first_assignment_start) and (second_assignment_stop >= first_assignment_stop)):
                complete_overlaps += 1

            #part 2
#            if (second_assignment_start <= first_assignment_start <= second_assignment_stop) or (second_assignment_start <= first_assignment_stop <= second_assignment_stop):
#            if (first_assignment_start <= second_assignment_start <= first_assignment_stop <= second_assignment_stop) or (second_assignment_start <= first_assignment_start <= second_assignment_stop <= first_assignment_stop):
#                partial_overlaps_strict += 1
#    partial_overlaps = complete_overlaps + partial_overlaps_strict
            first_assignment_range  = range(first_assignment_start,first_assignment_stop+1)
            second_assignment_range = range(second_assignment_start,second_assignment_stop+1)
            if any(first_section in second_assignment_range for first_section in first_assignment_range):
                partial_overlaps += 1
    print(f'{complete_overlaps = }')
    print(f'{partial_overlaps = }')



if __name__=='__main__':
    main()
