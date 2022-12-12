INPUT = 'input.txt'

def parse_line(line):
    if line.startswith('$ cd'):
        change_dir = line.split(' ')[-1]
        return {'change_dir': change_dir}
    elif line.startswith('$ ls'):
        return None
    elif line.startswith('dir'):
        sub_dir = line.split(' ')[-1]
        return {'new_sub_dir': sub_dir}
    elif len(line_split:=line.split(' '))==2 and line_split[0].isdigit():
        size, file = line_split
        size = int(size)
        return {'new_file': (file, size)}
    else:
        raise Exception(f'Unknown instruction: {line}')

def update_filesystem(filesystem, current_dir, new_sub_dir=None, new_file=None):
    if new_sub_dir is not None:
        command = ''.join(['filesystem'] + [f'[\'{directory}\']' for directory in current_dir+[new_sub_dir]]) + ' = {}'
    if new_file is not None:
        command = ''.join(['filesystem'] + [f'[\'{directory}\']' for directory in current_dir]) + '.update([new_file])'
    exec(command)
    return filesystem

def parse_input(input_file):
    filesystem  = {'root' : {}}
    current_dir = []
    with open(input_file) as input_data:
        for line in input_data.readlines():
            line = line.strip()
            line = line.replace('/', 'root')
            instruction = parse_line(line)
            if instruction is None: continue
            if 'change_dir' in instruction:
                if instruction['change_dir']=='..':
                    current_dir.pop()
                else:
                    current_dir.append(instruction['change_dir'])
            else:
                filesystem = update_filesystem(filesystem, current_dir, **instruction)
    return filesystem

def compute_dir_size(path, content, directory_sizes={}):
    size = 0
    for name, size_or_subdir in content.items():
        if isinstance(size_or_subdir, int):
            size += size_or_subdir
        else:
            subdir_path = '/'.join([path,name])
            if not subdir_path in directory_sizes:
                directory_sizes = compute_dir_size(subdir_path, size_or_subdir, directory_sizes)
            size += directory_sizes[subdir_path]
    directory_sizes[path] = size
    return directory_sizes

def main():
    filesystem = parse_input(INPUT)
    directories = compute_dir_size('root', filesystem['root'])

    #part 1
    tot_size_of_small_directories = 0
    for size in directories.values():
        if size<=100000:
            tot_size_of_small_directories += size
    print(f'{tot_size_of_small_directories = }')

    #part 2
    TOTAL_DISK_SPACE = 70000000
    NEEDED_SPACE     = 30000000

    space_to_be_freed = directories['root'] - (TOTAL_DISK_SPACE-NEEDED_SPACE)
    if space_to_be_freed>0:
        candidates_to_delete = (size for size in directories.values() if size>space_to_be_freed)
    size_of_smallest_deleteable_directory = min(candidates_to_delete)
    print(f'{size_of_smallest_deleteable_directory = }')


if __name__=='__main__':
    main()
