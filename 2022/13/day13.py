INPUT = 'input.txt'

def compare(left, right):
    for left_el, right_el in zip(left, right):
        if isinstance(left_el, int) and isinstance(right_el, int):
            if left_el==right_el:
                continue
            else:
                if left_el<right_el:
                    return True
                elif left_el>right_el:
                    return False
        else:
            if isinstance(left_el, int):
                comparison = compare([left_el], right_el)
            elif isinstance(right_el, int):
                comparison = compare(left_el, [right_el])
            else:
                comparison = compare(left_el, right_el)
            if comparison is not None:
                return comparison
    if len(left)<len(right):
        return True
    elif len(left)>len(right):
        return False
    else:
        return None


def find_valid_pairs(input_file):
    with open(input_file) as input_data:
        left_iter = input_data.readlines()[::3]
    with open(input_file) as input_data:
        right_iter = input_data.readlines()[1::3]
    for pair_idx, (left_str, right_str) in enumerate(zip(left_iter, right_iter), start=1):
        left  = eval(left_str)
        right = eval(right_str)
        #print(left, right)
        if compare(left, right):
            yield pair_idx


def main():
    valid_pairs = find_valid_pairs(INPUT)
    print(f'{sum(valid_pairs) = }')


if __name__=='__main__':
    main()
