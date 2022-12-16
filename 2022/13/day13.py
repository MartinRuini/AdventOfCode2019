import itertools

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


def find_index(packet_list, packet):
    if len(packet_list)==0:
        return 0
    elif len(packet_list)==1:
        idx = 1 if compare(packet_list[0], packet) else 0
        return idx
    else:
        half_length = len(packet_list)//2
        if compare(packet, packet_list[half_length]):
            idx = find_index(packet_list[:half_length], packet)
            return idx
        else:
            idx_second_half = find_index(packet_list[half_length:], packet)
            return half_length+idx_second_half


def sort_packets(input_file):
    sorted_packets = []
    with open(input_file) as input_data:
        for line in itertools.chain(input_data.readlines(), ['[[2]]', '[[6]]']):
            line = line.strip()
            if line:
                packet = eval(line)
                idx = find_index(sorted_packets, packet)
                sorted_packets.insert(idx, packet)
                if packet in ([[2]], [[6]]):
                    yield idx
    #return sorted_packets


def main():
    #part 1
    valid_pairs = find_valid_pairs(INPUT)
    print(f'{sum(valid_pairs) = }')

    #part 2
    decoder_key = 1
    for idx in sort_packets(INPUT):
        decoder_key *= idx+1
    print(f'{decoder_key = }')


if __name__=='__main__':
    main()
