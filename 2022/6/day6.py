from pdb import set_trace

INPUT = 'input.txt'

def is_marker(string):
    if len(string)==len(set(string)):
        return True
    return False

def main():
    length_of_marker = {
            'packet'  : 4,
            'message' : 14
            }
    with open(INPUT) as input_data:
        stream = input_data.readline().strip()

    for type_of_marker, length in length_of_marker.items():
        for i in range(length-1,len(stream)):
            if is_marker(stream[i-length+1:i+1]):
                print(f'Start-of-{type_of_marker} marker detected after receiving character {i+1}')
                break

if __name__=='__main__':
    main()
