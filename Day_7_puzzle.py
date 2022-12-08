def get_input():
    with open('Day_7_input.txt') as puzzle_input:
        txt = puzzle_input.readlines()
        raw_input = []
        for line in txt:
            raw_input.append(line.rstrip('\n'))
        return raw_input

def map_directories(dos_cmds):
    current_dir = []
    dir_sizes = {}
    for cmd in dos_cmds:
        if cmd == '$ cd ..':
            current_dir.pop()
        elif '$ cd' in cmd:
            if not current_dir:
                dir_name = cmd.split()[-1]
            else:
                dir_name = current_dir[-1] + cmd.split()[-1]
            current_dir.append(dir_name)
            dir_sizes[current_dir[-1]] = 0
        elif cmd == '$ ls' or 'dir' in cmd:
            pass
        else:
            for dir in range(len(current_dir)):
                dir_sizes[current_dir[dir]] += int(cmd.split()[0])
    return dir_sizes

def main():
    dos_cmds = get_input()
    dir_sizes = map_directories(dos_cmds)
    part1 = 0
    for dir in dir_sizes:
        if dir_sizes[dir] <= 100000:
            part1 += dir_sizes[dir]
    print(part1)
    free_space = 70000000 - dir_sizes['/']
    needed_space = 30000000 - free_space
    choices = []
    for dir in dir_sizes:
        if dir_sizes[dir] >= needed_space:
            choices.append(dir_sizes[dir])
    print(min(choices))

if __name__ == '__main__':
    main()