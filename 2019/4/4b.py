"""
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
How many different passwords within the range given in your puzzle input meet all of the criteria?

Your puzzle input is still 248345-746315.
"""
from timeit import default_timer as timer

def check_doubles(value):
    tmp = ""
    count = 0
    for digit in value:
        if tmp != digit:
            tmp = digit
            if count == 1:
                return True
            else:
                count = 0
        else:
            count = count + 1
    if count == 1:
        return True
    else:
        return False


def check_value(value):
    tmp = "0"
    for digit in value:
        if tmp > digit:
            return False
        else:
            tmp = digit
    return True


def run(range_):
    count = 0
    for value in range_:
        if check_doubles(str(value)) and check_value(str(value)):
            count = count + 1

    return count

def main():
    input_ = range(248345, 746316)
    start_time = timer()
    result = run(input_)
    time = timer() - start_time
    print(f'The answer is {result}. Time: {time}')


main()
