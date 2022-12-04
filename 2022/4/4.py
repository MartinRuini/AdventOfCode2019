INPUT = 'input.txt'

def main():
    complete_overlaps = 0
    partial_overlaps = 0
    with open(INPUT) as input_data:
        for line in input_data.readlines():
            first_assignment, second_assignment = line.strip().split(',')
            first_assignment_start, first_assignment_stop = map(int, first_assignment.split('-'))
            second_assignment_start, second_assignment_stop = map(int, second_assignment.split('-'))

            first_assignment_range  = range(first_assignment_start,first_assignment_stop+1)
            second_assignment_range = range(second_assignment_start,second_assignment_stop+1)

            #part 1
            #if ((first_assignment_start <= second_assignment_start) and (first_assignment_stop >= second_assignment_stop)) or ((second_assignment_start <= first_assignment_start) and (second_assignment_stop >= first_assignment_stop)): # faster
            if ((first_assignment_start in second_assignment_range) and (first_assignment_stop in second_assignment_range)) or ((second_assignment_start in first_assignment_range) and (second_assignment_stop in first_assignment_range)): # medium
            #if all(first_section in second_assignment_range for first_section in first_assignment_range) or all(second_section in first_assignment_range for second_section in second_assignment_range): # slower
                complete_overlaps += 1

            #part 2
            if any(first_section in second_assignment_range for first_section in first_assignment_range):
                partial_overlaps += 1
    print(f'{complete_overlaps = }')
    print(f'{partial_overlaps = }')



if __name__=='__main__':
    main()
