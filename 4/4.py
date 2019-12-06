"""
However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?

Your puzzle input is 248345-746315
"""
from timeit import default_timer as timer

def check_doubles(value):
    tmp = ""
    for digit in value:
        if tmp != digit:
            tmp = digit
        else:
            return True
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
    input_ = range(248345, 746315)
    start_time = timer()
    result = run(input_)
    time = timer() - start_time
    print(f'The answer is {result}. Time: {time}')


main()
